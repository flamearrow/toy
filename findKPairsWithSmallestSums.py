from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
#
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
#
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums
#
# Example
# 1:
#
# Input: nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3
# Output: [[1, 2], [1, 4], [1, 6]]
# Explanation: The
# first
# 3
# pairs
# are
# returned
# from the sequence: [1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [11, 2], [7, 6], [11, 4], [11, 6]
# Example
# 2:
#
# Input: nums1 = [1, 1, 2], nums2 = [1, 2, 3], k = 2
# Output: [[1, 1], [1, 1]]
# Explanation: The
# first
# 2
# pairs
# are
# returned
# from the sequence: [1, 1], [1, 1], [1, 2], [2, 1], [1, 2], [2, 2], [1, 3], [1, 3], [2, 3]

class HeapNode:
    def __init__(self, left, right, sumVal):
        self.left = left
        self.right = right
        self.sumVal = sumVal

    def __lt__(self, other):
        return self.sumVal < other.sumVal


class Solution:
    # push (1, 1), then add (1, 2) and (2, 1) to heap
    #  later, if picked (a, b), add (a+1, b) and (a, b+1) into heap
    # use a set to save already pushed (p1, p2) in to the heap
    # use a heap to save and retrive the min pair
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        p1 = 0
        p2 = 0

        ret = [[nums1[p1], nums2[p2]]]

        heap = []
        visited = set()
        visited.add((1, 0))
        visited.add((0, 1))
        if len(nums1) > 1:
            heappush(heap, HeapNode(1, 0, nums1[1] + nums2[0]))
        if len(nums2) > 1:
            heappush(heap, HeapNode(0, 1, nums1[0] + nums2[1]))

        for i in range(1, k):
            heapNode = heappop(heap)  # this is the smmallest in the heap
            nextP1 = heapNode.left
            nextP2 = heapNode.right
            print(" nextP1, nextP2, sum", nextP1, nextP2, heapNode.sumVal)

            ret.append([nums1[nextP1], nums2[nextP2]])
            if nextP1 + 1 < len(nums1) and (nextP1 + 1, nextP2) not in visited:
                visited.add((nextP1 + 1, nextP2))
                heappush(heap, HeapNode(nextP1 + 1, nextP2, nums1[nextP1 + 1] + nums2[nextP2]))
            if nextP2 + 1 < len(nums2) and (nextP1, nextP2 + 1) not in visited:
                visited.add((nextP1, nextP2 + 1))
                heappush(heap, HeapNode(nextP1, nextP2 + 1, nums1[nextP1] + nums2[nextP2 + 1]))

        return ret


if __name__ == '__main__':
    print(Solution())