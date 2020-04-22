a = int(input())
ar = list(input())
count = 0
bc = []


level=valley=0
for i in range(a):
    if(ar[i]=='U'):
        level+=1
        if(level==0):
            valley+=1
    else:
        level-=1
    
print (valley)
