#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a1 = a
    b1 = b
    alice, bob = 0, 0
    for x in range(len(a)):
        if a[x] > b [x]:
            alice = alice+1
        if a[x] < b [x]:
            bob = bob+1
    return alice,bob
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
