#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    pos = []
    neg = []
    zero = []

    for x in arr:
        if x > 0:
            pos.append(x)
        elif x < 0:
            neg.append(x)
        else:
            zero.append(x)

    print(len(pos) / n)
    print(len(neg) / n)
    print(len(zero) / n)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
