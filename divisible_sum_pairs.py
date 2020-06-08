n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


def divisibleSumPairs(n, k, arr):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if((arr[i]+arr[j])%k==0):
                count+=1
    return count


print(divisibleSumPairs(n,k,arr))
