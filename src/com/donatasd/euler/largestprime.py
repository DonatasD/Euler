__author__ = 'don'

def largestPrime(number, max):
    if (number == 1):
        return(max)
    for i in range(2,1000000):
        if (number % i == 0):
            if (max < i):
                max = i
            return(largestPrime(number / i, max))

print(largestPrime(600851475143,0))