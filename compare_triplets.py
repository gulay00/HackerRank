#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    a_score = 0
    b_score = 0

    for x in range(len(a)):
        if a[x] > b[x]:
            a_score += 1
        elif a[x] < b[x]:
            b_score += 1
        else:
            continue

    return a_score, b_score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
