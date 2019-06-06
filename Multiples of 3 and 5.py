#get the sum of multiples of 3 or 5 where the multiples are up to n.
def sum(n):
    sum = 0
    for i in range (3, n):
        if ((i % 3 == 0) or (i % 5 == 0)):
            sum += i
    return sum

if __name__ == '__main__':
    print(sum(1000))