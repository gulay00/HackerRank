#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1

    max_count = max(counts.values())
    return min([k for k, v in counts.items() if v == max_count])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
