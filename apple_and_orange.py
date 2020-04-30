s,t = map(int,input().split())
app,orr = map(int,input().split())
al,ol = map(int,input().split())
a_r = [int(x) for x in input().split()]
o_r = [int(x) for x in input().split()]

a_r1, o_r1 = [],[]
a, o = 0,0


for x in a_r:
    temp = x+app
    a_r1.append(temp)
    if temp >=s and temp <=t:
        a += 1
for y in o_r:
    temp = y+orr
    o_r1.append(temp)
    if temp >=s and temp <=t:
        o += 1

print(a,o,sep = "\n")
