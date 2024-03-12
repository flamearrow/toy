from treeNode.treeNode import TreeNode


def traverse_in_order(root: TreeNode, results):
    if root:
        traverse_in_order(root.left, results)
        results.append(root.val)
        traverse_in_order(root.right, results)


class BSTIteratorStupid:
    def __init__(self, root: TreeNode):

        # self.root = root
        # self.visited = {}
        self.numbers = []
        traverse_in_order(root, self.numbers)
        self.current_index = -1

    def next(self) -> int:
        self.current_index += 1
        return self.numbers[self.current_index]

    def hasNext(self) -> bool:
        return self.current_index < len(self.numbers)-1

    def hasPrev(self) -> bool:
        return self.current_index > 0

    def prev(self) -> int:
        # self.current_index -= 1
        self.current_index = 0 if self.current_index == 0 else self.current_index - 1
        return self.numbers[self.current_index]


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.to_visit = []
        self.current = root
        while self.current.left:
            self.to_visit.append(self.current)
            self.current = self.current.left

    def next(self) -> int:
        ret = self.current
        if ret.right:  # need to visit right
            cur = ret.right
            while cur.left:
                self.to_visit.append(cur)
                cur = cur.left
            self.current = cur
        else:  # need to pop
            if self.to_visit:
                self.current = self.to_visit.pop(-1)
            else:
                self.current = None

        return ret.val

    def hasNext(self) -> bool:
        return self.current is not None


if __name__ == '__main__':
    # root = TreeNode(1, 2)
    # root.left.set_left(left_value=3).set_right(right_value=7)
    # root.left.set_right(right_value=4).set_right(right_value=5)
    # # stp = BSTIteratorStupid(root)
    # stp = BSTIterator(root)
    # while stp.hasNext():
    #     print(stp.next())

    root = TreeNode(7, 3, 15)
    root.right.set_left(left_value=9)
    root.right.set_right(right_value=20)
    stp = BSTIteratorStupid(root)
    print(stp.next())
    print(stp.prev())
    print(stp.next())
    print(stp.next())
    print(stp.hasNext())
    print(stp.next())
    print(stp.next())
    print(stp.next())
    print(stp.hasNext())
    print(stp.hasPrev())
    print(stp.prev())
    print(stp.prev())

