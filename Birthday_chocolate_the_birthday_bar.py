def chocolate(arr, total, limit):
    adds = []
    result = 0

    while len(arr) > limit-1:
        temp = sum(arr[:limit])
        adds.append(temp)
        del arr[0]
    
    for x in adds:
        if x == total:
            result += 1
    return result
    
if __name__ == "__main__":
    size = int(input())
    arr = [int(x) for x in input().split()]
    total, limit = [int(x) for x in input().split()]
    print(chocolate(arr,total,limit))
