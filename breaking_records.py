#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    max_r = scores[0]
    min_r = scores[0]
    max_c = 0
    min_c = 0

    for x in range(1, len(scores)):
        if scores[x] > max_r:
            max_r = scores[x]
            max_c += 1
        elif scores[x] < min_r:
            min_r = scores[x]
            min_c += 1

    return max_c, min_c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
