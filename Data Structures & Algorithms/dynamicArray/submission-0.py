class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity < 0:
            capacity = 0
        self.arr = [None] * capacity
        self.capacity = capacity
        self.len = 0

    def get(self, i: int) -> int:
        # if i >= capacity:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()
        self.arr[self.len] = n
        self.len = self.len + 1

    def popback(self) -> int:
        ele = self.arr[self.len - 1]
        self.arr[self.len - 1] = None
        self.len = self.len - 1
        return ele

    def resize(self) -> None:
        self.arr.extend([None] * self.capacity)
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.len
    
    def getCapacity(self) -> int:
        return self.capacity

