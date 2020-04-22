a = int(input())
ar = list(map(int,input().split()))
freq = {}

for x in ar:
    freq[x] = ar.count(x)

only_value = list(freq.values())

count = [int(x/2) for x in only_value]

print(sum(count))
