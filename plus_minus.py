n = int(input())
arr = list(map(int,input().split()))
zero, pos, neg = 0,0,0
for x in arr:
    if x == 0:
        zero = zero+1
    if x > 0:
        pos = pos+1
    if x < 0:
        neg = neg+1

print("{0:.6f}".format(pos/n))
print("{0:.6f}".format(neg/n))
print("{0:.6f}".format(zero/n))
