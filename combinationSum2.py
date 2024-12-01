# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations


from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque

class Solution:
    def __init__(self):
        pass

    # backtrack:
    #  starting from beginning of list,
    #    for each item, take it, then recursively look at the rest of the list
    #  this works by simulating BINARY tree, the index identifies a tree
    #   * when an item is taken, its appended to the list,
    #       meaning we go left
    #       then left tree is probed with the rest of the list after
    #          params are (i+1, listWithItem)
    #   * when an item is NOT taken, its skipped by going to next iteration of for loop
    #       meaning we go right
    #       then right tree is also probed with the rest of the list after
    #          params are (i+1, listWithItem)
    #
    # !NOTE: the for loop doesn't build a multi leg tree, it's a BINARY tree
    #
    #
    #
    # dedup: only TAKE(go LEFT) of a tree when an item is the first of a consecutive string
    #   because all right consecutive nodes will be considered as the subtree after the first
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates = sorted(candidates)

        def probe(curIndex, curList, remaining):
            if remaining == 0:
                ret.append(curList[:])
            elif remaining < 0:
                return
            else:
                for i in range(curIndex, len(candidates)):
                    if i > curIndex and candidates[i] == candidates[i - 1]:
                        continue
                    curList.append(candidates[i])
                    probe(i + 1, curList, remaining - candidates[i])
                    curList.pop()

        probe(0, [], target)
        return ret


if __name__ == '__main__':
    print(Solution().combinationSum2([1, 2, 3], 7))