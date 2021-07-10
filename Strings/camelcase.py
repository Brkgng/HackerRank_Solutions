#!/bin/python3

import math
import os
import random
import re
import sys

#
#
# See the problem
# https://www.hackerrank.com/challenges/camelcase/problem
#
#


def camelcase(s):
    # Write your code here
    return sum(1 for char in s if char.isupper()) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
