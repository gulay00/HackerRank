#!/bin/python3
import os

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribe = 0

    for i in range(len(q)):
        # If someone has moved forward by more than 2 positions, it's too chaotic
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        # Count inversions in the limited window where bribes could have happened
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribe += 1

    print(bribe)


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
