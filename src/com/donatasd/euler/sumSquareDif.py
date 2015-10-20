

def squareSum(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i * i
    return sum


def sumSquare(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum * sum


print(sumSquare(100) - squareSum(100))