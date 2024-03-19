from functools import reduce

def testZip():
    l = [1,2,3,4]
    def is_sorted(l):
        ll = zip(l, l[1:]) # zip creates a list of pair of length the min of the two, so this is a pariwise
        return all(x < y for (x, y) in ll)

    print(is_sorted(l))


def testReduce(l):
    sum = reduce(lambda x, y: x + y, l) # with initial value, the first element will be initial value
    print(sum)


def testStack():
    stack = list()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    while stack:
        print(stack.pop())

from queue import Queue
import heapq


def testQueue():
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    while not q.empty():
        print(q.get())

from collections import deque
def testdeque():
    print("deque as queue")
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    while queue:
        print(queue[0])
        print(queue.popleft())

    print("deque as stack")
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    while stack:
        print(stack[0])  # peek
        print(stack.pop())


def testPriorityQueue():
    heapQ = [23,4,2,11,4214]
    heapq.heapify(heapQ)
    while heapQ:
        print(heapq.heappop(heapQ))

if __name__ == '__main__':
    # l = [1, 2, 3, 4, 5]
    # l[1], l[2], l[3] = l[2], l[3], l[1]
    # doubleL = list(map(lambda i: i*2, l))
    # print(doubleL)
    # filteredL = list(filter(lambda i: i % 2 == 0, l))
    # print(filteredL)
    # testZip()
    # testReduce([1, 2, 4, 3])
    # print(min(2, 1))
    # testStack()
    # testQueue()
    # testPriorityQueue()
    testdeque()

