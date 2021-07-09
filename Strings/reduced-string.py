#
# See the problem
# https://www.hackerrank.com/challenges/reduced-string/problem
#
#

def superReducedString(s):
    strLen = len(s) - 1
    i = 0
    while i < strLen:
        if s[i] == s[i+1]:
            s = s[0:i] + s[i+2:]
            strLen -= 2
            i = -1
            if not s:
                return "Empty String"
        i += 1
    return s


if __name__ == '__main__':
    s = input()
    result = superReducedString(s)
    print(result)
