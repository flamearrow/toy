# Given two integers a and b, return any string s such that:
#
# s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.

# Example 1:
#
# Input: a = 1, b = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# Example 2:
#
# Input: a = 4, b = 1
# Output: "aabaa


# apart from bitmap, can have the gredy algorithm, if previous 2 is aa/bb, then append b/a, otherwise append the larger
def strWithout3a3b(a: int, b: int) -> str:
    ret = ""
    while a or b:
        if a < 0 or b < 0:
            return "No" # otherwise will go beyond 0, can't create a good match
        if ret[-2:] == "aa":
            ret += "b"
            b -= 1
        elif ret[-2:] == "bb":
            ret += "a"
            a -= 1
        elif a > b:
            ret += "a"
            a -= 1
        else:
            ret += "b"
            b -= 1

    return ret


def strWithout3a3bBitMap(a: int, b: int) -> str:
    # a 1 and b 0, e.g 11100, keep minus
    bitMap = ((1 << a) - 1) << b

    # has a 1 and b 0, and doesn't have conscutives
    def isValid(bitMapNum):
        bStr = bin(bitMapNum)[2:] # filter 0B11000 to 11000
        leading0Count = (a+b) - len(bStr)
        if leading0Count >= 3:
            return False
        if bStr.count("1") != a:
            return False
        for index in range(1, len(bStr)-1): # ! exclusive!
            if bStr[index-1] == bStr[index] == bStr[index+1]:
                return False
        return True

    while bitMap >= 0:
        if isValid(bitMap): # has a 1 and b 0, and doesn't have conscutives
            # b = bin(bitMap)
            ret = ""
            for i in range(0, a+b):
                if ((1 << i) & bitMap) > 0:
                    ret = ret + "a"
                else:
                    ret = ret + "b"
            return ret[::-1]
        else:
            bitMap -= 1
    return ""


if __name__ == '__main__':
    # print(strWithout3a3b(4, 3))

    print(strWithout3a3bBitMap(4, 3))