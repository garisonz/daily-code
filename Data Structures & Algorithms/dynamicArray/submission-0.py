class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity cannot be less than or equal to zero")
        
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            temp = self.arr[self.length - 1]
            self.arr[self.length - 1] = 0
            self.length -= 1
            return temp

    def resize(self) -> None:
        self.capacity *= 2
        temp = [0] * self.capacity

        for i in range(len(self.arr)):
            temp[i] = self.arr[i]

        self.arr = temp

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
    