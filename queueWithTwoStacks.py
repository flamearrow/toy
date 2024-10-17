class MyQueue:

    def __init__(self):
        self.inStack = list()  # only use append and pop
        self.outStack = list()

    def push(self, x: int) -> None:
        # push to inStack
        self.inStack.append(x)

    def pop(self) -> int:
        # pop from out stack, if empty, shuffle items from in to out
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self) -> int:
        # peek from out stack, if empty, shuffle items from in to out
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self) -> bool:
        return len(self.inStack) >= 0 and len(self.outStack) >= 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == '__main__':
    q = MyQueue()
    print()