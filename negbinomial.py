import numpy as np

def prob(n, p, r):
    '''
    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :param r: số lần thành công mà đạt được thì ngừng
    :return: xác suất của sympol thứ n
    '''
    if n < r:
        return 0

    p = (np.math.factorial(n - 1) / (np.math.factorial(n - r) * (np.math.factorial(r - 1)))) * (p ** r) * ((1 - p) ** (n - r))
    return p


def infoMeasure(N, p, r):
    '''
    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :param r: số lần thành công mà đạt được thì ngừng
    :return: lượng tin của sympol thứ n
    '''

    if N < r:
        return 0

    return -np.log2(prob(N, p, r))


def sumProb(N, p, r):
    '''
    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :param r: số lần thành công mà đạt được thì ngừng
    :return: tổng xác suất của các sympols
    Vì không gian mẫu có N sympol nên tổng xác suất của N sympol đó phải bằng 1.
    Thực nghiệm:
    - Khi N = 100 sumProb = 0.9999999999999999 ~ 1.0
    - Khi N = 1000 sumProb = 0.9999999999999999 ~ 1.0
    '''

    sumProp = 0
    for k in range(r, N + 1):
        sumProp += prob(k, p, r)

    return sumProp

def approxEntropy(N, p, r):
    '''
    :param N: tổng số sympol
    :param p:xác suất bernoulli
    :param r: số lần thành công mà đạt được thì ngừng
    :return: xấp xỉ entropy của nguồn thông tin
    Thực nghiệm:
    - Với N = 100, entropy = 4.150775320863947
    - Với N = 1000, entropy = 4.150775320863947
    '''

    entropy = 0
    for k in range(r, N + 1):
        entropy += prob(k, p, r) * infoMeasure(k, p, r)

    return entropy


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = prob(3, 0.5, 2)
    print(p)

    i = infoMeasure(3, 0.5, 2)
    print(i)

    sumP = sumProb(1000, 0.5, 10)
    print(sumP)

    entropy = approxEntropy(1000, 0.5, 10)
    print(entropy)
