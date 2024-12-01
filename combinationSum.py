from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def search(cur, candidateIndex):
            print("cur", cur)
            if sum(cur) == target:
                ret.append(cur[:])
                return
            if sum(cur) > target:
                return

            for i in range(candidateIndex, len(candidates)):
                cur.append(candidates[i])
                search(cur, i)
                cur.pop()
            return

        search([], 0)
        return ret

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def prob(curCan, curList, remaining):
            if remaining == 0:
                ret.append(curList)
            else:
                if curCan:
                    c = curCan[0]
                    curCount = 0
                    while curCount * c <= remaining:
                        prob(curCan[1:], curList + [c] * curCount, remaining - curCount * c)
                        curCount += 1

        prob(candidates, [], target)
        return ret

    # backtrack idea:
    #  each probe() function starts from a position and generates all possible combinations hereafter
    #  its impl is as follows:
    #     starting from canIdx to end, try take each candidate, then continue probing after that candidate[inclusive]
    #  each interation, it takes an item from a position and move to next position[inclisve]
    #  since we may take an item mutiple times, we don't recusively call the one after, but the same index
    #  the next iteration will skip the previous one and start from after
    def combinationSumBacktrack(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def probe(curList, canIdx, remaining):
            if remaining < 0:
                return
            elif remaining == 0:
                ret.append(curList[:])
            else:
                for i in range(canIdx, len(candidates)):
                    curList.append(candidates[i])
                    probe(curList, i, remaining - candidates[i]) # start from i+1 if an item can only be used once
                    curList.pop()

        probe([], 0, target)
        return ret


if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7))