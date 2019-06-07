def sumOfSquares(n):
    sum = 0
    for i in range(1, n+1, 1):
        sum += (i ** 2)
    return sum

def squareOfSum(n):
    sum = 0
    for i in range(1, n+1, 1):
        sum += i
    return (sum ** 2)

if __name__ == '__main__':
    print(squareOfSum(100) - sumOfSquares(100))