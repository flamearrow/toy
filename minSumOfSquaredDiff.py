import heapq

# You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.
#
# The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.
#
# You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.
#
# Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.
#
# Note: You are allowed to modify the array elements to become negative integers

from typing import List


class Solution:
    # this is faster as we're trying to decase min(left, maxCount) each time
    # save a map of {diffValue, diffValueCount}
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # diffIndexArr = []
        diffCountMap = {}
        n = len(nums1)
        for i in range(n):
            key = -abs(nums1[i] - nums2[i])
            if key not in diffCountMap:
                diffCountMap[key] = 1
            else:
                diffCountMap[key] = diffCountMap[key] + 1

        diffCountArr = list(diffCountMap.items())
        heapq.heapify(diffCountArr)

        left = k1 + k2
        while left > 0:
            # find the smallest (largest after -)
            maxDiff, diffCount = heapq.heappop(diffCountArr)

            if maxDiff == 0:
                break
            else:
                if left > diffCount:
                    # minus one for each maxDiff, remvoe head
                    newKey = maxDiff + 1
                    if diffCountArr[0] == newKey:  # previous is newKey, just add the count
                        diffCountArr[1] += diffCount
                    else:
                        # no new key, create an new entry
                        heapq.heappush(diffCountArr, (newKey, diffCount))
                    left -= diffCount
                else:
                    newKey = maxDiff + 1

                    # add new key
                    if diffCountArr[0][0] == newKey:  # previous is newKey, just add the count
                        key, count = heapq.heappop(diffCountArr)
                        heapq.heappush(diffCountArr, (key, count + left))
                    else:
                        # no new key, create an new entry
                        heapq.heappush(diffCountArr, (newKey, left))

                    # decrease count of current key if it has left
                    if left < diffCount:
                        heapq.heappush(diffCountArr, (maxDiff, diffCount - left))

                    left = 0

        return sum([a[0] * a[0] * a[1] for a in diffCountArr])

    # this is slow as we're only decreasing the max diff by one each time
    def minSumSquareDiffOneByOne(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffIndexArr = []
        n = len(nums1)
        for i in range(n):
            heapq.heappush(diffIndexArr, ((-abs(nums1[i] - nums2[i]), i)))

        for i in range(k1 + k2):
            # find the smallest (largest after -)
            maxDiff, index = heapq.heappop(diffIndexArr)
            if maxDiff == 0:
                break
            else:
                maxDiff += 1  # maxDiff must be below 0
                heapq.heappush(diffIndexArr, (maxDiff, index))

        return sum([a[0] * a[0] for a in diffIndexArr])


if __name__ == '__main__':
    # print(Solution().minSumSquareDiff([1, 4, 10, 12], [5, 8, 6, 9], 1, 1))
    v = 0
    for i in [1, 2, 4, 5, 5]:
        v = (v ^ i)

    print(v)

    
