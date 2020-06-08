import collections

def migratoryBirds(arr):
    counter = dict(collections.Counter(arr))
    values = max(list(counter.values()))

    return min([int(x) for x,y in counter.items() if y == values])

n = int(input())
arr = [int(x) for x in input().split()]
print(migratoryBirds(arr))
