class Deque:

    def __init__(self):
        self.dq = deque()

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def append(self, value: int) -> None:
        self.dq.append(value)

    def appendleft(self, value: int) -> None:
        self.dq.appendleft(value)

    def pop(self) -> int:
        return self.dq.pop() if self.dq else -1

    def popleft(self) -> int:
        return self.dq.popleft()
