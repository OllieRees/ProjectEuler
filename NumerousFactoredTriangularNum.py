import math

def numFactors(n):
    numFactors = 2
    factors = list()
    termCond = math.ceil(math.sqrt(n)) + 1
    for fact in range(2, termCond):
        if(n % fact == 0 and not(factors.__contains__(fact))):
            factors.append(fact)
            factors.append(n//fact)
            numFactors += 2

    if(math.sqrt(n) == math.floor(math.sqrt(n))):
        numFactors -= 1

    return numFactors

def triangularNumberDivisor(divisorLim):
    triNum = 1
    n = 2
    while(numFactors(triNum) <= divisorLim):
        print(triNum)
        triNum += n
        n += 1
    return triNum

if __name__ == '__main__':
    print(triangularNumberDivisor(500))