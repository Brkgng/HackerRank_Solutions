#!/bin/python3

import math
import os
import random
import re
import sys

#
#
# See the problem
# https://www.hackerrank.com/challenges/diagonal-difference/problem
#
#


def diagonalDifference(arr):
    lengthCol = len(arr[0])
    primary = sum(arr[i][i] for i in range(lengthCol))
    secondary = sum(arr[i][lengthCol - i - 1] for i in range(lengthCol))
    return abs(primary - secondary)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
