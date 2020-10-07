import numpy as np

def prob(n, p, N):
    p = (np.math.factorial(N) / (np.math.factorial(n) * (np.math.factorial(N - n)))) * (p ** n) * ((1 - p) ** (N - n))
    return p


def infoMeasure(n, p, N):
    return -np.log2(prob(n, p, N))


def sumProb(N, p):
    sumProp = 0
    for k in range(1, N + 1):
        sumProp += prob(k, p, N)
    return sumProp

def approxEntropy(N, p):
    entropy = 0
    for k in range(0, N + 1):
        entropy += prob(k, p, N) * infoMeasure(k, p, N)

    return entropy


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = prob(2, 0.5, 2)
    print(p)

    i = infoMeasure(2, 0.5, 3)
    print(i)

    sumP = sumProb(1000, 0.5)
    print(sumP)

    entropy = approxEntropy(1000, 0.5)
    print(entropy)