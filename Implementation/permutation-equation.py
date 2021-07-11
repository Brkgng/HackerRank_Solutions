#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
# https://www.hackerrank.com/challenges/permutation-equation/problem
#
#


def permutationEquation(p):
    n = []
    for i in range(1, len(p)+1):
        find = p.index(i) + 1
        n.append(p.index(find) + 1)
    return n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
