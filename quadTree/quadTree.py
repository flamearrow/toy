# Used for searching locations, each node has up to four points(x, y) or four sub nodes,
# covering area defined by x, y, width, height. Keep adding nodes to its points(capacity), then subdivide and
# redistribute existing points into its sub node
class QuadTreeNode:
    def __init__(self, x, y, width, height, capacity=4):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.capacity = capacity
        self.points = []
        self.topLeft = None
        self.topRight = None
        self.bottomLeft = None
        self.bottomRight = None

    def divided(self):
        return self.topLeft is not None

    def insert(self, x, y):
        if x < self.x or x > self.x + self.width or y < self.y or y > self.y + self.height:
            # not in the region
            return False

        if len(self.points) < self.capacity:
            self.points.append((x, y))
        else:
            self.divide()
            # recursively insert ino its 4 sub divisions, try it one by one
            if (not self.topLeft.insert(x, y) and
                not self.topRight.insert(x, y) and
                not self.bottomLeft.insert(x, y) and
                not self.bottomRight.insert(x, y)):
                raise Exception("fail to insert point", x, y, "into this quadNode")

    def divide(self):
        halfWidth = self.width // 2
        halfHeight = self.height // 2
        # (x, x+halfWidth)
        self.topLeft = QuadTreeNode(self.x, self.y, width=halfWidth, height=halfHeight, capacity=self.capacity)
        # (x+halfWidth+1, x+width)
        self.topRight = QuadTreeNode(self.x + halfWidth + 1, self.y, width=halfWidth, height=halfHeight,
                                     capacity=self.capacity)
        self.bottomLeft = QuadTreeNode(self.x, self.y + halfHeight + 1, width=halfWidth, height=halfHeight,
                                       capacity=self.capacity)
        self.bottomRight = QuadTreeNode(self.x + halfWidth + 1, self.y + halfHeight + 1, width=halfWidth,
                                        height=halfHeight, capacity=self.capacity)

        for (x, y) in self.points:
            if (not self.topLeft.insert(x, y)
                and not self.topRight.insert(x, y)
                and not self.bottomLeft.insert(x, y)
                and not self.bottomRight.insert(x, y)):
                raise Exception("failed to insert ", x, y, "into any of subdivisions")
        self.points.clear()

    # check if x, y is in this quad tree
    def query(self, x, y):
        if x < self.x or x > self.x + self.width or y < self.y or y > self.y + self.height:
            # not in the region
            return False
        for (pX, pY) in self.points:
            if x == pX and y == pY:
                return True

        # divided, four quads are non null
        if self.divided():
            return (self.topLeft.query(x, y) or
                    self.topRight.query(x, y) or
                    self.bottomLeft.query(x,y) or
                    self.bottomRight.query(x, y))

    # query all nodes within a certain area
    def queryArea(self, x, y, width, height):
        # if not overlap with the node, return []
        if x + width < self.x or self.x + self.width < x or y + height < self.y or self.y + self.height < y:
            return []
        ret = []
        # check if this Treenode.points is within area
        for pX, pY in self.points:
            if x <= pX <= x + width and y <= pY <= y + height:
                ret.append([pX, pY])
        if self.divided():
            ret += self.topLeft.queryArea(x, y, width, height)
            ret += self.topRight.queryArea(x, y, width, height)
            ret += self.bottomLeft.queryArea(x, y, width, height)
            ret += self.bottomRight.queryArea(x, y, width, height)
