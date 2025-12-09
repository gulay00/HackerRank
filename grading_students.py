#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    grades2 = []
    onluq = 0
    for x in grades:
        if x > 37:
            onluq = x // 10
            if (((onluq + 1) * 10) - x) < 3:
                grades2.append((onluq + 1) * 10)
            elif (((onluq * 10) + 5) - x) < 3 and (((onluq * 10) + 5) - x) > 0:
                grades2.append((onluq * 10) + 5)
            else:
                grades2.append(x)
        else:
            grades2.append(x)
    return grades2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
