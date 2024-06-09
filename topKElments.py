# Given
# an
# integer
# array
# nums and an
# integer
# k,
# return the
# k
# most
# frequent
# elements.You
# may
# return the
# answer in any
# order.
#
# Example
# 1:
#
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
# Example
# 2:
#
# Input: nums = [1], k = 1
# Output: [1]

from typing import List
def topKFrequent(nums: List[int], k: int):
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    # return map(lambda x: x[0], sorted(count.items(), key=lambda x: -x[1])[:k])

    def selectKth(vCPair, k):
        # sort by count, use first as pivot
        left = list(filter(lambda x: x[1] < vCPair[0][1], vCPair))
        mid = list(filter(lambda x: x[1] == vCPair[0][1], vCPair))
        right = list(filter(lambda x: x[1] > vCPair[0][1], vCPair))
        if len(right) == k:  # there are k values larger than pivot
            return right
        elif len(right) > k:  # need to go right
            return selectKth(right, k)
        else:  #
            residue = k - len(right)
            if residue <= len(mid):
                return right + mid[:residue]
            else:
                return right + mid + selectKth(left, residue-len(mid))

    kLargestPairs = selectKth(list(count.items()), k)

    return list(map(lambda x: x[0], kLargestPairs))

if __name__ == '__main__':
    print(topKFrequent(nums=[1,1,1,2,2,3], k=3))