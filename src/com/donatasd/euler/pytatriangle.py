import math
# a + b + c = 1000
# a^2 + b^2 = c^2
# a < b < c


def check(a,b) :
    c = math.sqrt(a ** 2 + b ** 2)
    # print(a + b + c == 1000)
    # print(a < b < c)
    # print(a**2 + b**2 == c**2)
    # print(str(a) + " " + str(b) + " " + str(c))
    # print(a + b + c)
    # print(a*b*c)
    return a + b + c == 1000 and a < b < c and a**2 + b**2 == c**2


def guess():
    for i in range(100,500):
        for j in range(100,500):
            if check(i,j):
                print(str(i) + " " + str(j) + " " + str(1000 - i - j))
                return i * j * (1000 - i - j)


guess()
#check(200,375)

