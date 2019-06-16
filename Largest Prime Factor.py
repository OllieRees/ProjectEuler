#check if n is prime
def isPrime(n):
    if (n == 1):
        return False
    for fact in range(2, n):
        if(n % fact == 0):
            return False
    return True


# Get the largest prime factor of n
def largestPrimeFactor(n):
    if (isPrime(n)):
        return n

    #thinking about n as a multiplication of primes.
    fact = 2
    while (n > 1):
        while(n % fact == 0):
            n = n/fact
        fact += 1

    return fact - 1

if __name__ == '__main__':
    n = 600851475143
    print(largestPrimeFactor(n))