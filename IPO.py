from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ret = [0]

        def dfs(currentCap, projectsTaken):
            print(" currentCap {}, projectsTaken {}".format(currentCap, projectsTaken))
            if len(projectsTaken) == k or len(projectsTaken) == len(profits):
                ret[0] = max(ret[0], sum([profits[i] for i in projectsTaken]))
            else:
                for project in range(len(profits)):
                    if project not in projectsTaken and currentCap >= capital[project]:
                        print(" taking project", project)
                        dfs(currentCap - capital[project] + profits[project], projectsTaken + [project])

        dfs(w, [])
        return ret[0]


if __name__ == '__main__':
    print(Solution().findMaximizedCapital(1, 2, [1,2,3], [1,1,2]))