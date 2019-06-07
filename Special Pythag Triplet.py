import math

def addsUpTo1000(a, b):
    return ( a + b + math.sqrt(a ** 2 + b ** 2) ) == 1000

def getProduct(a, b):
    return a * b * math.sqrt(a ** 2 + b ** 2)

def findSpecialTriplet():
    for a in range(1, 500):
        for b in range(1, 500):
            if(addsUpTo1000(a, b) == True):
                return getProduct(a, b)
    return 0

if __name__ == '__main__':
    print(findSpecialTriplet())
