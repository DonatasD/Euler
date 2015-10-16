def smallestMultiple(max):
    for j in range(1,max):
        for i in range(1,21):
            if (j % i != 0):
                break
            if (i == 20):
                return(j)

#print(smallestMultiple(99999999))
sum = 1
for i in range(1,21):
    sum *= i

print sum
