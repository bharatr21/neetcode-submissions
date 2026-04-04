class MinStack:

    def __init__(self):
        self.st = []
        self.min = math.inf

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
            self.st.append((val, val))
        else:
            self.st.append((val, self.min))

    def pop(self) -> None:
        self.st.pop()
        self.min = self.st[-1][1] if self.st else math.inf

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.min
