from math import sqrt
from functools import reduce

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

arr_size = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
all_factors, d = [], []

for x in b:
    c = factors(x)
    all_factors.append(c)
common = set.intersection(*all_factors)

for x in range(len(a)):
    temp = {int(y) for y in common if y % a[x] == 0}
    d.append(temp)

final = set.intersection(*d)
print(len(final))
