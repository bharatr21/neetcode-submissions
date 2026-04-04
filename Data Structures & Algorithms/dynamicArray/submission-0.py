class DynamicArray:
    
    def __init__(self, capacity: int):
        self.res = []
        self.cap = capacity


    def get(self, i: int) -> int:
        return self.res[i]

    def set(self, i: int, n: int) -> None:
        self.res[i] = n

    def pushback(self, n: int) -> None:
        if len(self.res) == self.cap:
            self.resize()
        self.res.append(n)

    def popback(self) -> int:
        return self.res.pop()

    def resize(self) -> None:
        self.cap = self.cap * 2


    def getSize(self) -> int:
        return len(self.res)
    
    def getCapacity(self) -> int:
        return self.cap