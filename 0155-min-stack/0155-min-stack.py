class MinStack:

    def __init__(self):
        self.stack = []
        self.lowest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.lowest:
            if val <= self.lowest[-1]:
                self.lowest.append(val)
        else:
            self.lowest.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.lowest and val == self.lowest[-1]:
            self.lowest.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return 0
        

    def getMin(self) -> int:
        if self.lowest:
            return self.lowest[-1]
        return 0
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()