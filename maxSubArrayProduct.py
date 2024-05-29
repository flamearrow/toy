from typing import List
class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     maxIncludingI = nums[0]
    #     maxStart = 0
    #     minIncludingI = nums[0]
    #     minStart = 0
    #     retStart = 0
    #     retEnd = 0
    #
    #     ret = maxIncludingI
    #
    #     for i in range(1, len(nums)):
    #         cur = nums[i]
    #         tmp = max(cur, cur*maxIncludingI, cur*minIncludingI)
    #         minIncludingI = min(cur, cur*maxIncludingI, cur*minIncludingI)
    #         if minIncludingI == cur:
    #             minStart = i
    #         maxIncludingI = tmp
    #         ret = max(ret, maxIncludingI)
    #         if ret == maxIncludingI:  # found the largest range, update current range
    #             if tmp == cur:
    #                 maxStart = i
    #                 rangeStart = maxStart
    #             elif tmp == cur*maxIncludingI:
    #                 rangeStart = maxStart
    #             else:
    #                 rangeStart = minStart
    #
    #             retStart = rangeStart
    #             retEnd = i
    #
    #     print("retStart", retStart)
    #     print("retEnd", retEnd)
    #     print("result", maxIncludingI)
    #     return ret

    def maxProduct(self, nums: List[int]) -> int:
        maxIncludingI = nums[0]
        minIncludingI = nums[0]
        ret = maxIncludingI
        retStart, retEnd = 0, 0
        maxStart, minStart = 0, 0

        for i in range(1, len(nums)):
            cur = nums[i]
            tmp = max(cur, cur * maxIncludingI, cur * minIncludingI)

            maxFromCur, maxFromMax, maxFromMin = False, False, False
            if tmp == cur:
                maxStart = i
                maxFromCur = True
            elif tmp == cur*maxIncludingI:
                maxFromMax = True
            else:
                maxFromMin = True

            minIncludingI = min(cur, cur * maxIncludingI, cur * minIncludingI)

            if minIncludingI == cur:
                minStart = i

            maxIncludingI = tmp
            ret = max(ret, maxIncludingI)
            if ret == maxIncludingI: # found a new largest, update range
                retEnd = i
                if maxFromCur:
                    retStart = i
                elif maxFromMax:
                    retStart = maxStart
                elif maxFromMin:
                    retStart = minStart

        print("retStart: ", retStart)
        print("retEnd: ", retEnd)
        print(ret)
        return ret


if __name__ == '__main__':
    Solution().maxProduct([2, 3, -2])
