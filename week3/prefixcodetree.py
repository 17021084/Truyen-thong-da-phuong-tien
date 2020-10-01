from typing import List
import json 

class PrefixCodeTree:
    def __init__(self):
        self.data: dict = {}

    def json(self):
        return self.data

    def insert(self, codeword: List[int], symbol: str) -> None:
        current_node: dict = self.data
        for bit in codeword:
            if bit == 0:
                if current_node.get("0") is None:
                    current_node.__setitem__("0", {})
                current_node = current_node.get("0")
            else:
                if current_node.get("1") is None:
                    current_node.__setitem__("1", {})
                current_node = current_node.get("1")
        current_node.__setitem__("leaf", symbol)

    @staticmethod
    def _hex_to_binary(bytes_literal: bytes) -> str:
        hex_string: str = bytes_literal.hex()
        decimal: int = int(hex_string, base=16)
        binary_string = bin(decimal)[2:]
        return binary_string

    def decode(self, encodedData: bytes, datalen: int) -> List[List[str]]:
        binary_string = PrefixCodeTree._hex_to_binary(encodedData)
        tree = self.json()
        current_node = tree

        symbols: List[str] = []
        codeword: str = ""
        codewords: List[str] = []
        loop_len = min(datalen, binary_string.__len__())

        for i in range(loop_len):
            bit: str = binary_string[i]
            codeword += bit
            current_node = current_node.get(bit)
            if "leaf" in current_node:
                symbols.append(current_node.get("leaf"))
                codewords.append(codeword)
                codeword = ""
                current_node = tree

        unused_bits = binary_string[loop_len:]
        codewords.append(unused_bits)

        return [codewords, symbols]


# Test
codebook: dict = {
    "x1": [0],
    "x2": [1, 0, 0],
    "x3": [1, 0, 1],
    "x4": [1, 1]
}


codeTree = PrefixCodeTree()

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

try:
    json_string = json.dumps(codeTree.json(), indent=2, sort_keys=True)
    print(json_string)

    bits, symbols = codeTree.decode(b"\xd2\x9f\x20", 21)
    for bit in bits:
        print(str(bit).ljust(4, ' '), end="")

    print()
    for symbol in symbols:
        print(symbol.ljust(4, ' '), end="")
except TypeError:
    print("String cant decode")
