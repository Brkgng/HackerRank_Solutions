#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
#
# https://www.hackerrank.com/challenges/encryption/problem
#


def encryption(s):
    lengthS = len(s)
    col = (lengthS ** 0.5)
    if col % 1 != 0:
        col += 1
    col = int(col)
    output = ""
    for i in range(col):
        while lengthS > i:
            output += s[i]
            i += col
        output += " "
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
