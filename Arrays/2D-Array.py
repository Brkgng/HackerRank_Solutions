#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
#
# https://www.hackerrank.com/challenges/2d-array/problem
#


def hourglassSum(arr):
    # output can be at least -63 so initial value is -64
    output = -64
    for i in range(4):
        for j in range(4):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] \
                              + arr[i+1][j+1] + \
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if total > output:
                output = total
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
