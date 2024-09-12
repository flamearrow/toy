# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):

    def itob(N):
        ret = ""
        while N > 0:
            ret = str((N&1)) + ret
            N = N >> 1
        return ret

    # b = bin(N)[2:]
    b = itob(N)
    longest = 0
    curLen = 0

    for c in b:
        if c == '0':
            curLen += 1
        else:
            if curLen > 0:
                longest = max(longest, curLen)
            curLen = 0
    return longest


a = [2,1,4]
a.sort()
print(a)