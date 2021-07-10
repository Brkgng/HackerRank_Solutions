#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
# https://www.hackerrank.com/challenges/mars-exploration/problem
#
#


def marsExploration(s):
    o = 1
    changed = 0
    for i in range(len(s)):
        if i == o:
            o += 3
            if s[i] != 'O':
                changed += 1
        else:
            if s[i] != 'S':
                changed += 1
    return changed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
