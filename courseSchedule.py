from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # canonical topological sort
        # from->to : from is the prerequisite, to is the course
        # fromNode: [toNode]
        # use a queue to add all the nodes without incoming course
        # add more ndoes to the queue when its incoming edge drops to 0
        # O(m+n) - m is edge(buidl adj), n is nodes(build incoming edges)
        self.adj = {}
        # toNode: #ofFromnode
        self.incomingEdge = {}

        for f, t in prerequisites:
            if f not in self.adj:
                self.adj[f] = []
            self.adj[f].append(t)

            if f not in self.incomingEdge:  # use to calculate all nodes
                self.incomingEdge[f] = 0
            if t not in self.incomingEdge:
                self.incomingEdge[t] = 0
            self.incomingEdge[t] += 1

        q = deque()

        for node, incomingEdge in self.incomingEdge.items():
            if incomingEdge == 0:
                q.append(node)

        courseTaken = 0
        while len(q) > 0:
            nextNode = q.popleft()
            courseTaken += 1
            if nextNode in self.adj:
                for n in self.adj[nextNode]:
                    self.incomingEdge[n] -= 1
                    if self.incomingEdge[n] == 0:
                        q.append(n)

        return courseTaken == len(self.incomingEdge)

    # build course: [pre] first, try to remove one per time, update eacht ime
    def canFinishNaive(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course: [preReqCourses]
        cReq = {}
        for course, reqCourse in prerequisites:
            if course not in cReq:
                cReq[course] = set()
            if reqCourse not in cReq:
                cReq[reqCourse] = set()
            cReq[course].add(reqCourse)

        def removeNextValidCourse():
            courseToReturn = None
            for course in cReq:
                if len(cReq[course]) == 0:
                    courseToReturn = course
                    break
            if courseToReturn is not None:
                del cReq[courseToReturn]
                print(" got", courseToReturn)
                return courseToReturn
            else:
                return None

        nextCourse = removeNextValidCourse()
        while nextCourse is not None:
            for course in cReq:
                if nextCourse in cReq[course]:
                    cReq[course].remove(nextCourse)
            nextCourse = removeNextValidCourse()

        return len(cReq) == 0


if __name__ == '__main__':
    print(Solution())
