import sys
from collections import deque
import heapq

def reorganizeString(s: str) -> str:
    cCount = {}
    for c in s:
        cCount[c] = cCount[c] + 1 if c in cCount else 1

    countItemList = list(map(lambda x: (-x[1], x[0]), cCount.items()))
    heapq.heapify(countItemList)
    ans = []
    while countItemList:
        firstCount, firstChar = heapq.heappop(countItemList)
        if not ans or ans[-1] != firstChar:
            ans.append(firstChar)
            if firstCount+1 < 0:
                heapq.heappush(countItemList, (firstCount+1, firstChar))
        else:
            if not countItemList:
                return ""
            secondCount, secondChar = heapq.heappop(countItemList)
            ans.append(secondChar)
            if secondCount+1 < 0:
                heapq.heappush(countItemList, (secondCount+1, secondChar))
            heapq.heappush(countItemList, (firstCount, firstChar))
    return "".join(ans)

def isAnagram(s: str, t: str) -> bool:
    buffer = [0] * 26
    for c in s:
        buffer[ord(c) - ord('a')] += 1

    for c in t:
        buffer[ord(c) - ord('a')] -= 1

    print(buffer)
    return not any([i != 0 for i in buffer])

def strStr(haystack: str, needle: str) -> int:
    buffer = [0] * 26
    for c in needle:
        buffer[ord(c) - ord('a')] += 1

    start, end = 0, 0  # [)
    while end < len(haystack):
        nextC = haystack[end]
        if buffer[ord(nextC) - ord('c')] > 0:
            buffer[ord(nextC) - ord('c')] -= 1
            end += 1
            print(f"now end: {end}, start: {start}")
            if end - start == len(needle):
                return True
        else:
            startC = haystack[start]
            buffer[ord(startC) - ord('c')] += 1
            start += 1
            if start > end:
                end = start
    return False


def arrComparisonToy():
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 4]
    arr3 = [1, 3, 4]

    if arr1 <= arr2 <= arr3:
        print("wow")

    arr1S = [str(i) for i in arr1]
    arr2S = [str(i) for i in arr2]
    arr3S = [str(i) for i in arr3]

    if arr1S <= arr2S <= arr3S:
        print("wow")

    if "05" < "12":
        print("wor")

    if "2013" < "2113":
        print("ww")


if __name__ == '__main__':
    # reorganizeString("aaab")
    # a = min(1,2,3)
    # print(a)
    #
    # i = -sys.maxsize-1
    # j = 23
    # ret = max(i, j)
    # print(ret)
    # toy = [1,2,3,4]
    # print(isAnagram("anagram", "nagaram"))
    # print(strStr("abcabfw", "abc"))
    # l = [1,2,3]
    # l.popleft()

    # s = deque()
    # s.append(1)
    # s.append(2)
    # s.append(3)
    # s.append(4)
    #
    # print(s[0])
    arrComparisonToy()
