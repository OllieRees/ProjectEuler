import math

#check if n is prime
def isPrime(n):
    if (n == 1):
        return False

    for fact in range(2, math.floor(math.sqrt(n)) + 1):
        if(n % fact == 0):
            return False
    return True

def primeSieve(list):
    for e in list:
        if(e != 2 and e % 2 == 0):
            list.remove(e)
        elif(e != 3 and e % 3 == 0):
            list.remove(e)
        elif(e != 5 and e % 5 == 0):
            list.remove(e)
        elif(e != 7 and e % 7 == 0):
            list.remove(e)
        elif(e != 11 and e % 11 == 0):
            list.remove(e)
    return list

#sum primes that are lower than prime_lim
def sumPrimes(prime_lim):
    sum = 0
    for n in range(2, prime_lim):
        if(isPrime(n)):
            sum += n
    return sum

if __name__ == '__main__':
    print(sumPrimes(2000000))