class MinStack:

    def __init__(self):
        self.min_stack = []
        self.main_stack = []

        

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
            self.main_stack.append(val)
            return
        if (val <= self.min_stack[-1]):
            self.min_stack.append(val)

        self.main_stack.append(val)

    def pop(self) -> None:
        if not self.main_stack:
            return
        temp = self.main_stack[-1]
        if temp == self.min_stack[-1]:
            self.min_stack.pop()
        self.main_stack.pop()
        

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]
        return 0
        

    def getMin(self) -> int:

        if self.min_stack:
            return self.min_stack[-1]
        return 0

        
