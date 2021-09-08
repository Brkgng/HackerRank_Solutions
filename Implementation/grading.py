#!/bin/python3

import math
import os
import random
import re
import sys

#
# See the problem
#
# https://www.hackerrank.com/challenges/grading/problem
#


def gradingStudents(grades):
    for idx in range(len(grades)):
        if grades[idx] < 38:
            continue
        nextMultipleOf5 = (grades[idx] // 5 + 1) * 5
        if nextMultipleOf5 - grades[idx] < 3:
            grades[idx] = nextMultipleOf5
    return grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
