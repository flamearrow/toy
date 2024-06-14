class TreeNode:
    def __init__(self, root_value, left_value=None, right_value=None):
        self.val = root_value
        if left_value:
            self.left = TreeNode(root_value=left_value)
        else:
            self.left = None
        if right_value:
            self.right = TreeNode(root_value=right_value)
        else:
            self.right = None

    def __str__(self):
        return "{}".format(self.val)

    def set_left(self, left_value=None):
        self.left = TreeNode(root_value=left_value)
        return self.left

    def set_right(self, right_value=None):
        self.right = TreeNode(root_value=right_value)
        return self.right


def in_order_t(rootNode: TreeNode):
    if rootNode:
        in_order_t(rootNode.left)
        print(rootNode.val)
        in_order_t(rootNode.right)


if __name__ == '__main__':
    root = TreeNode(1, 2, right_value=5)
    root.right.set_left(9).set_left(8)

    in_order_t(root)
