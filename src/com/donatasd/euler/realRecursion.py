import math


def g(a, x):
    if x < a:
        return 1
    else:
        return g(a, x-1) + g(a, x-a)


def G(n):
    return g(math.sqrt(n), n)


print(G(10000009))