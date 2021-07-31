#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
#
# https://www.hackerrank.com/challenges/quicksort1/problem
#
#


def quickSort(arr):
    left = []
    right = []
    for i in arr[1::]:
        if arr[0] > i:
            left.append(i)
        else:
            right.append(i)
    left.append(arr[0])
    return left + right


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
