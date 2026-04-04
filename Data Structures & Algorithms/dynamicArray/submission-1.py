class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.length = 0
        self.res = [0] * capacity


    def get(self, i: int) -> int:
        return self.res[i]

    def set(self, i: int, n: int) -> None:
        self.res[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.cap:
            self.resize()
        self.res[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.res[self.length]


    def resize(self) -> None:
        self.cap = self.cap * 2
        tmp = [0] * self.cap

        for i in range(self.length):
            tmp[i] = self.res[i]
        self.res = tmp


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.cap