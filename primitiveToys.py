def removeDuplicates(s: str) -> str:
    left, right = 0, 1
    while right < len(s):
        if right - left == 2:
            s = s[0:left] + s[right:]
            left -= 1
            if left < 0:
                left = 0
            right = left + 1
        if s[right] == s[left]:
            right += 1
        else:
            left = right
            right += 1
    if right - left == 2:
        s = s[0:left]
    return s


if __name__ == '__main__':
    removeDuplicates("abbaca")