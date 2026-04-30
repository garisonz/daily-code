class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        temp = self.arr[self.getSize()]
        self.arr[self.getSize()] = 0
        return temp

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        temp = self.arr + [0] * self.capacity
        self.arr = temp

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity