from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:

    # the idea: find the mid or A and B, leaving Aleft, Aright, Bleft, Bright, since A and B all sorted, we know that
    #   if A[mid] > B[mid], then Bleft < Bright & Aright, and Aright > Aleft & Bleft
    #   if A[mid] < B[mid], then Aleft < Aright & Bright, and Bright > Bleft & Aleft
    #  so  know there are guaranteed _____ to the right of the range or to the left of the range
    #  ________***
    #  ***_______
    # to find kth,
    #  if k>A[mid]+B[mid], it must be in the second half, we discard the left of smaller array
    #  if k<A[mid]+B[mid], it must be in the first half, we discard the right of larger array

    # the algorithm can find the kth largest number of two sorted arrays in O(log(M+N)) time
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        totalLen = len1 + len2

        # find the kth largest value in the combined array of nums1[left1:right1+1] and nums2[left2:right2+1]
        def findKth(k, left1, right1, left2, right2):
            if left1 > right1:  # nothing in left, right the kth in nums2
                return nums2[k - left1]
            if left2 > right2:
                return nums1[k - left2]

            mid1, mid2 = (left1 + right1) // 2, (left2 + right2) // 2
            midVal1, midVal2 = nums1[mid1], nums2[mid2]

            if midVal1 > midVal2:
                if mid1 + mid2 < k:
                    # discard smaller half of 2
                    return findKth(k, left1, right1, mid2 + 1, right2)
                else:
                    # discard larger half of 1
                    return findKth(k, left1, mid1 - 1, left2, right2)
            else:
                if mid1 + mid2 < k:
                    # discard smaller half of 1
                    return findKth(k, mid1 + 1, right1, left2, right2)
                else:
                    # discard larger half of 2
                    return findKth(k, left1, right1, left2, mid2 - 1)

        if totalLen % 2 == 0:
            # need the average of totalLen//2 and (totalLen-1)//2
            return (findKth(totalLen // 2, 0, len1 - 1, 0, len2 - 1) + findKth((totalLen - 1) // 2, 0, len1 - 1, 0,
                                                                               len2 - 1)) / 2
        else:
            # need the value of totalLen//2
            return findKth(totalLen // 2, 0, len1 - 1, 0, len2 - 1)

    def findKthOfSortedArrays(self, k, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        # find the kth largest value in the combined array of nums1[left1:right1+1] and nums2[left2:right2+1]
        def findKth(k, left1, right1, left2, right2):
            if left1 > right1:  # nothing in left, return the kth in nums2
                return nums2[k - left1]
            if left2 > right2:
                return nums1[k - left2]

            mid1, mid2 = (left1 + right1) // 2, (left2 + right2) // 2
            midVal1, midVal2 = nums1[mid1], nums2[mid2]

            if midVal1 > midVal2:
                if mid1 + mid2 < k:
                    # discard smaller half of 2
                    return findKth(k, left1, right1, mid2 + 1, right2)
                else:
                    # discard larger half of 1
                    return findKth(k, left1, mid1 - 1, left2, right2)
            else:
                if mid1 + mid2 < k:
                    # discard smaller half of 1
                    return findKth(k, mid1 + 1, right1, left2, right2)
                else:
                    # discard larger half of 2
                    return findKth(k, left1, right1, left2, mid2 - 1)

        return findKth(k, 0, len1 - 1, 0, len2 - 1)


if __name__ == '__main__':
    for k in range(0, 6):
        print(Solution().findKthOfSortedArrays(k, [1, 3, 5], [2, 4, 6]))
