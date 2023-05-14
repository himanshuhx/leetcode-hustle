# using two stacks
class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini:
            self.mini.append(val)
        else:
            self.mini.append(min(val, self.mini[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mini.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.mini:
            return self.mini[-1]

# O(1) time O(N) space


class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mini = val
        else:
            if val < self.mini:
                self.stack.append((2*val)-self.mini)
                self.mini = val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val < self.mini:
            self.mini = (2*self.mini)-val

    def top(self) -> int:
        if self.stack[-1] < self.mini:
            return self.mini
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
