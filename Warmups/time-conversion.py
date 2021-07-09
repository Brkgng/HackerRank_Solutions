#
# See the problem
# https://www.hackerrank.com/challenges/time-conversion/problem
#
#

def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        return s[:-2]
    if s[:2] == "12":
        return s[:-2]
    return str(int(s[:2]) + 12) + s[2:-2]


# if __name__ == '__main__':
    # s = input()
    # print(timeConversion(s))

n = 10 / 2
print( 2 % -2 == 0)
