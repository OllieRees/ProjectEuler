
def divisibleUpTo20(n):
    for i in range(1, 21):
        if(n % i != 0):
            return False
    return True

def smallestMultiple():
    for i in range (2520, 2432902008176640000, 20):
        if (divisibleUpTo20(i) == True):
            return i

if __name__ == '__main__':
    print (smallestMultiple())