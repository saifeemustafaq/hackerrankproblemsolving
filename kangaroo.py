x1, v1, x2, v2 = map(int,input().split())

a = "NO"
for x in range(10000):
    if x1 == x2:
        a = "YES"
        break
    else:
        x1 = x1+v1
        x2 = x2+v2
        
print(a)
