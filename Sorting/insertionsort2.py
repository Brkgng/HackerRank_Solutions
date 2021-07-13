#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
# https://www.hackerrank.com/challenges/insertionsort2/problem
#
#


def insertionSort2(n, arr):
    for i in range(1, n):
        check = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > check:
                arr[j+1] = arr[j]
                arr[j] = check
        print(*arr, sep=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
