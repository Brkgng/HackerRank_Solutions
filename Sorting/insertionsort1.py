#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
# https://www.hackerrank.com/challenges/insertionsort1/problem
#
#


def insertionSort1(n, arr):
    last = arr[-1]
    for i in range(n-1, 0, -1):
        if last < arr[i-1]:
            arr[i] = arr[i-1]
            print(*arr, sep=" ")
        else:
            arr[i] = last
            print(*arr, sep=" ")
            return
    arr[0] = last
    print(*arr, sep=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
