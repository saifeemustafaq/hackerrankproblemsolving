import math

n = int(input())
ar,ar1 = [],[]

for x in range(n):
    ar.append(int(input()))

for x in ar:
    if x < 38:
        ar1.append(x)
    elif x >= 38:
        temp = math.ceil(x/5)
        temp = temp*5
        temp2 = temp-x
        if temp2 < 3:
            ar1.append(temp)
        else:
            ar1.append(x)

print(*ar1,sep = "\n")
