import numpy as np


def prob(n, p):
    '''
  :param N: sum of  sympols
    :param p: probability of bernoulli
    :return: probaility of sympol at n
    '''

    p = 1 / (2 ** n)
    return p

'''
    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :return: lượng thông tin của sympol của thứ n
'''

def infoMeasure(n, p):
    return -np.log2(prob(n, p))

'''
    :param N: sum of  sympols
    :param p: probability of bernoulli
    :return : sum of probability
   
'''
def sumProb(N, p):


    sumProp = 0
    for k in range(1, N + 1):
        sumProp += prob(k, p)

    return sumProp

'''
    :param N: sum of sympols
    :param p: probability of  bernoulli
    :return:  approximately entropy value s of information sources
  
    -  N = 100, entropy = 1.9999999999999998 ~ 2
    -  N = 1000, entropy = 1.9999999999999998 ~ 2
'''
def approxEntropy(N, p):
  

    sumInfo = 0
    for k in range(1, N + 1):
        sumInfo += prob(k, p) * infoMeasure(k, p)

    return sumInfo


if __name__ == '__main__':
    p = prob(2, 0.5)
    print(p)

    i = infoMeasure(2, 0.5)
    print(i)

    sumProp = sumProb(1000, 0.5)
    print(sumProp)

    entropy = approxEntropy(1000, 0.5)
    print(entropy)
