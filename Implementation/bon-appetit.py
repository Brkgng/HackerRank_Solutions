#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
# https://www.hackerrank.com/challenges/bon-appetit/problem
#
#


def bonAppetit(bill, k, b):
    total = sum(x for x in bill)
    actual = (total - bill[k]) // 2
    if actual == b:
        print("Bon Appetit")
    else:
        print(b - actual)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
