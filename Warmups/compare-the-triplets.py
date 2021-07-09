#!/bin/python3

import math
import os
import random
import re
import sys

#
#
# See the problem
# https://www.hackerrank.com/challenges/compare-the-triplets/problem
#
#
#


def compareTriplets(a, b):
    liste = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            liste[0] += 1
        elif a[i] < b[i]:
            liste[1] += 1
    return liste


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
