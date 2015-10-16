
def evenfib(prev,curr,sum):
    #print(curr)
    if (curr > 4000000):
        return(sum)
    if (curr % 2 == 0):
        sum += curr
    return(evenfib(curr, curr + prev, sum))

print(evenfib(1,1,0))