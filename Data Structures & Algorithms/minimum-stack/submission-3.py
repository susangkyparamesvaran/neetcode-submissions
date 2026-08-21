class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.min_stack) > 0):
            minimum = min(self.min_stack[-1],val)
            self.min_stack.append(minimum)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        pop_val = self.stack[-1]
        return pop_val

    def getMin(self) -> int:
        return self.min_stack[-1]
