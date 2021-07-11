#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
#
#


def breakingRecords(scores):
    most = least = 0
    maximum = minimum = scores[0]
    for score in scores:
        if maximum < score:
            maximum = score
            most += 1
        elif minimum > score:
            minimum = score
            least += 1
    return [most, least]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
