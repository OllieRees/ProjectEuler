#check if n is prime
def isPrime(n):
    if (n == 1):
        return False
    if(n == 2):
        return True

    for fact in range(2, round(n/4)):
        if(n % fact == 0):
            return False
    return True

#sum primes that are lower than prime_lim
def sumPrimes(prime_lim):
    sum = 0
    for n in range(2, prime_lim):
        if(isPrime(n)):
            sum += n
    return sum

if __name__ == '__main__':
    print(sumPrimes(2000000))