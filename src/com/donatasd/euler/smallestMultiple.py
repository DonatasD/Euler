def check(n, range):
    for i in range(2, (range + 1)):
        if(n % i != 0):
            return False
    return True

max = 1
for i in range(2,21):
    max = max * i

for i in range(21,1,-1):
    if (check(max / i, 20)):
        max = max / i

print max