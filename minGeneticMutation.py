from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        queue = deque()
        queue.append([startGene, 0])

        def diffByOne(f, t):
            diffByOne = False
            for i in range(8):
                if f[i] != t[i]:
                    if diffByOne:
                        return False
                    else:
                        diffByOne = True
            return diffByOne

        def mutationFrom(gene):
            ret = []
            for g in bank:
                if g not in visited and diffByOne(gene, g):
                    print("{} and {} is diff by one".format(gene, g))
                    ret.append(g)
            return ret

        while queue:
            nextG, step = queue.popleft()
            visited.add(nextG) # do the visited check when just popped
            if nextG == endGene:
                return step
            for nextMutation in mutationFrom(nextG):
                queue.append([nextMutation, step+1])
        return -1
