#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'countApplesAndOranges' function below.
#
# The function accepts:
# 1. INTEGER s
# 2. INTEGER t
# 3. INTEGER a
# 4. INTEGER b
# 5. INTEGER_ARRAY apples
# 6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_alma = 0
    count_orange = 0

    for alma in apples:
        if (a + alma) >= s and (a + alma) <= t:
            count_alma += 1

    for orange in oranges:
        if (b + orange) >= s and (b + orange) <= t:
            count_orange += 1

    print(count_alma)
    print(count_orange)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
