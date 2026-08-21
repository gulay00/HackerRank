#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    result = []

    for n in range(p, q + 1):
        square = n * n
        square_str = str(square)

        d = len(str(n))

        right = int(square_str[-d:])
        left = int(square_str[:-d]) if square_str[:-d] else 0

        if left + right == n:
            result.append(n)

    if result:
        print(*result)
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
