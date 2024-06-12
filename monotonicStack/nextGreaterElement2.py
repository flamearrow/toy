from typing import List
from collections import deque


def nextGreaterElements(nums: List[int]) -> List[int]:
    prevMap = {}
    numStack = deque()
    for num in nums:
        while numStack and numStack[-1] < num:  # find a pair
            prevMap[numStack.pop()] = num
        numStack.append(num)

    print(" stack size: ", len(numStack))
    print(numStack)


    for num in nums:
        # print("!!!! peeking", str(numStack[-1]), "and", str(num))
        while numStack and numStack[-1] < num:  # find a pair
            prevMap[numStack.pop()] = num

    print(" stack size: ", len(numStack))
    print(numStack)


    for num in numStack:
        prevMap[num] = -1


    return [prevMap.get(x, -1) for x in nums]


if __name__ == '__main__':
    input = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    print(nextGreaterElements(input))
