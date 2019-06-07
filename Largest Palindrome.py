import math

#Checks if n can be multipled by two three-digit numbers
def multipliedByThreeDigits(n):
    factors = list()
    for i in range(100, 1000):
        if (n % i == 0):
            other_fact = round(n/i)
            if(other_fact >= 100 and other_fact <= 999):
                return True
    return False

def isPalindrome(n):
    #turn n to separate digits
    revDigits = list()
    while(n >= 1):
        revDigits.append(n % 10)
        n = math.floor(n / 10)

    #reverse
    nDigits = list()
    for i in range(revDigits.__len__() - 1, -1, -1):
        nDigits.append(revDigits.__getitem__(i))

    return nDigits == revDigits

#gets the largest palindrome formed 2 3-digit numbers.
def largestPalindrome():
    n = 999 * 999
    #reduce n if it's not a palindrome and it's not multiplied by three digits
    while(n >= 100):
        if(isPalindrome(n) == True and multipliedByThreeDigits(n) == True):
            return n
        n -= 1
if __name__ == '__main__':
    print (largestPalindrome())