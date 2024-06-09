from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        cur = 0
        op = '+'
        for index, c in enumerate(s):
            if c.isdigit():
                cur = cur * 10 + int(c)
            if (c != ' ' and not c.isdigit()) or index == len(s) - 1:
                if op == '+':
                    stack.append(cur)
                elif op == '-':
                    stack.append(-cur)
                elif op == '*':
                    prev = stack.pop()
                    stack.append(cur * prev)
                elif op == '/':
                    prev = stack.pop()
                    stack.append((int)(prev / cur))

                op = c
                cur = 0
        ret = 0
        while stack:
            ret += stack.pop()
        return ret

    def calculate2(self, s: str) -> int:
        cur = 0
        prev = 0
        op = '+'
        ret = 0

        for index, c in enumerate(s):
            if c.isdigit():
                cur = cur * 10 + int(c)
            if not c.isdigit() and c != ' ' or index == len(s) - 1:
                if op == '+':
                    ret += prev
                    prev = cur
                elif op == '-':
                    ret += prev
                    prev = -cur
                elif op == '*':
                    prev = prev * cur
                elif op == '/':
                    prev = int(prev / cur)
                op = c
                cur = 0

        ret += prev
        return ret




if __name__ == '__main__':
    print(Solution().calculate2("3+2*2"))
