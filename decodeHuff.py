class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    ret = ""
    cur = root
    for c in s:
        if c == "1":
            if cur.right: # can still go right
                cur = cur.right
            else: # terminated, add and append
                ret += cur.data
                # c is consumed, reset to root.right
                cur = root.right
        elif c == "0":
            if cur.left: # can still go left
                cur = cur.left
            else: # terminated add and append
                ret += cur.data
                cur = root.left
    ret += cur.data

    return ret


if __name__ == '__main__':
    root = Node(5, None)
    root.left = Node(2, None)
    root.right = Node(1, "A")
    root.left.left = Node(1, "B")
    root.left.right = Node(1, "C")

    print(decodeHuff(root, "1"))

