from typing import List
class Solution:
    def maxWidthRampSort(self, nums: List[int]) -> int:
        arr = []
        for index, num in enumerate(nums):
            arr.append((num, index))
        arr.sort()

        minIndexSoFar = arr[0][1]
        ret = 0
        for i in range(1, len(arr)):
            value, index = arr[i]
            if index > minIndexSoFar:
                ret = max(ret, index - minIndexSoFar)
            minIndexSoFar = min(minIndexSoFar, index)
        return ret

    def maxWidthRamp(self, nums):
        n = len(nums)
        indices_stack = []

        # Fill the stack with indices in increasing order of their values
        for i in range(n):
            if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)

        max_width = 0

        # Traverse the array from the end to the start
        for j in range(n - 1, -1, -1):
            if not indices_stack:
                break
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                max_width = max(max_width, j - indices_stack[-1])
                # Pop the index since it's already processed
                indices_stack.pop()

        return max_width


if __name__ == '__main__':
    # print(Solution().maxWidthRamp([3, 5, 4, 6, 2, 7, 1]))
    # print(-5 % 4)
    # print(-5//4)
    c = "d"
    if c:
        print("b")

