def sumFibonacciSequence (n):
    sum = 2
    max_index = maxFibNum(n)
    a = 1 #f(n-1)
    b = 2 #f(n)
    for index in range(0, max_index):
        temp = a
        a = b
        b += temp
        if (b % 2 == 0):
            sum += b
    return sum

#return the largest value of n where f(n) < n.
def maxFibNum (n):
    i = 0
    a = 1 #f(n - 1)
    b = 2 #f(n)
    while (b < n):
        temp = a
        a = b
        b = b + temp #b is now f(n)
        i += 1
    return i


if __name__ == '__main__':
    print (sumFibonacciSequence(4000000))