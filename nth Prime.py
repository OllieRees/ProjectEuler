#check if n is prime
def isPrime(n):
    for fact in range(2, n):
        if(n % fact == 0):
            return False
    return True

#get the nth prime
def prime(n):
    i = 1
    p = 2
    while(i < n):
        if(isPrime(p)):
            i += 1
        p += 1
    return p

if __name__ == '__main__':
    print (prime(10001))