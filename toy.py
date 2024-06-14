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

if __name__ == '__main__':
    reorganizeString("aaab")


