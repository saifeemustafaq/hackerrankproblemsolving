n = int(input())
arr,arr1,arr2 = [],[],[]
y,z = 0,n-1

for x in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

for x in range(n):
    temp = arr[x][y]
    arr1.append(temp)
    y = y+1

for x in range(n):
    temp = arr[x][z]
    arr2.append(temp)
    z = z-1

print(abs(sum(arr1)-sum(arr2)))
