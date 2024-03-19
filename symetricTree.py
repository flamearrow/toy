from typing import List, Optional
from treeNode.treeNode import TreeNode
from queue import Queue

class Solution:
    def isSymmetric3(self, root: Optional[TreeNode]) -> bool:
        q = Queue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            n1 = q.get()
            n2 = q.get()
            if not n1 and not n2:
                continue
            if n1 and not n2:
                return False
            if n2 and not n1:
                return False
            if n1.val != n2.val:
                return False
            q.put(n1.left)
            q.put(n2.right)
            q.put(n1.right)
            q.put(n2.left)
        return True

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        def isS(left, right):
            if not left and not right:
                return True
            elif left and not right:
                return False
            elif right and not left:
                return False

            return left.val == right.val and isS(left.left, right.right) and isS(left.right, right.left)

        return isS(root.left, root.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = Queue()
        q.put(root)
        leftInLvl = 1

        def isS(curLvl):
            if len(curLvl) == 1:
                return True
            elif len(curLvl) % 2 == 1:
                return False
            else:
                half = len(curLvl) // 2
                left = curLvl[:half]
                right = curLvl[half:]
                right.reverse()
                print("left", left)
                print("right", right)
                return left == right

        curLvl = []
        while not q.empty():
            cur = q.get()
            if cur:
                curLvl.append(cur.val)
            else:
                curLvl.append(None)

            if cur:
                if cur.left:
                    q.put(cur.left)
                else:
                    q.put(None)
                if cur.right:
                    q.put(cur.right)
                else:
                    q.put(None)

            leftInLvl -= 1
            if leftInLvl == 0:
                if not isS(curLvl):
                    return False
                curLvl.clear()
                leftInLvl = q.qsize()

        return True
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.set_left(2).set_left(3)
    root.set_right(2).set_right(3)
    # root.left.set_left(4)
    # root.right.set_left(4)
    print(s.isSymmetric(root))
