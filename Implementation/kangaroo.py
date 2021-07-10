#
# See the problem
# https://www.hackerrank.com/challenges/kangaroo/problem
#
#

def kangaroo(x1, v1, x2, v2):
    # n is number of jumps so it should be
    # x1 + v1 * n = x2 + v2 * n
    if v1 == v2:
        return "NO"
    n = (x2 - x1) / (v1 - v2)
    if n >= 0 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)
