#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
#
# https://www.hackerrank.com/challenges/closest-numbers/problem
#


def closestNumbers(arr):
    arr = sorted(arr)
    min_list = [arr[0], arr[1]]
    minSub = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        sub = abs(arr[i] - arr[i+1])
        if (minSub < sub):
            continue
        elif (minSub > sub):
            minSub = sub
            min_list.clear()
        min_list.append(arr[i])
        min_list.append(arr[i+1])
    return min_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
