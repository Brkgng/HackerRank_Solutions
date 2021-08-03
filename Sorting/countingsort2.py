#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
#
# https://www.hackerrank.com/challenges/countingsort2/problem
#


def countingSort(arr):
    countArr = [0] * 100
    for i in arr:
        countArr[i] += 1
    resultArr = []
    for i in range(100):
        if (countArr[i] != 0):
            for j in range(countArr[i]):
                resultArr.append(i)
    return resultArr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
