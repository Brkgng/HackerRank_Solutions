#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
#
# https://www.hackerrank.com/challenges/array-left-rotation/problem
#


def rotateLeft(d, arr):
    if d == 0 or d > len(arr):
        return arr

    """ Brute force 
     for i in range(d):
       for j in range(len(arr) - 1):
          arr[j], arr[j+1] = arr[j+1], arr[j]
    """

    """ Optimization
    idx = d
    output = arr.copy()
    for i in range(len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        if (idx == len(arr) - 1):
            return arr[:len(arr)-d] + output[:d]
        else:
            idx += 1
    """

    # One line
    return arr[d:] + arr[:d]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
