class MinStack:
    def __init__(self):
        self.min_ = float('inf')
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val - self.min_ if self.arr else 0)
        self.min_ = val if len(self.arr) == 1 else min(self.min_, val)

    def pop(self) -> None:
        popped_val = self.arr.pop()

        if popped_val < 0:
            self.min_ = self.min_ - popped_val

    def top(self) -> int:
        return self.min_ + self.arr[-1] if self.arr[-1] > 0 else self.min_

    def getMin(self) -> int:
        return self.min_
        
