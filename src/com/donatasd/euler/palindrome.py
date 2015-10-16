
def maxPalindrome(max, min):
    result = None
    for i in range(max, min, -1):
        for j in range(max, min, -1):
            if (isPalindrome(i * j) and i * j > result):
                result = i * j
    return result
def isPalindrome(number):
    if(len(str(number))%2 == 1):
        return False
    for i in range(len(str(number))/2):
        if(str(number)[i] != str(number)[len(str(number)) - 1 - i]):
            return False
    return True

print(maxPalindrome(999,100))