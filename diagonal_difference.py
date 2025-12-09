#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diag_sum = 0
    right_diag_sum = 0
    z = 0

    for x in range(len(arr)):
        left_diag_sum += arr[x][x]

    for y in range(len(arr) - 1, -1, -1):
        right_diag_sum += arr[z][y]
        z += 1

    return abs(left_diag_sum - right_diag_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
