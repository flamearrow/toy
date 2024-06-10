from typing import List

# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.
#
# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # return 0 if there's no app to collect, or the total path length if there is
        visited = []
        def dfs(node):
            ret = 0
            unvisitedNeighbours = [x[1] for x in edges if x[0] == node and x[1] not in visited]
            unvisitedNeighbours += [x[0] for x in edges if x[1] == node and x[0] not in visited]
            visited.append(node)
            for unvisitedNeighbour in unvisitedNeighbours:
                neibourSteps = dfs(unvisitedNeighbour)
                # only add to result if either the neighbour has apple or its children has apple
                if neibourSteps > 0 or hasApple[unvisitedNeighbour]:
                    ret = ret + 2 + neibourSteps
            return ret
        return dfs(0)
