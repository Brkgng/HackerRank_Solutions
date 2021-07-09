#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
# https://www.hackerrank.com/challenges/plus-minus/problem
#
#


def plusMinus(arr):
    positive = negative = zero = 0
    lengthArr = len(arr)
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print(positive / lengthArr, negative /
          lengthArr, zero / lengthArr, sep="\n")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
