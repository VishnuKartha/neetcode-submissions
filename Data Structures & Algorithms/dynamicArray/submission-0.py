class DynamicArray:
    array = []
    size = 0

    def __init__(self, capacity: int):
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.size += 1
        if(self.size > len(self.array)):
            self.resize()
        self.array[self.size - 1] = n

    def popback(self) -> int:
        self.size -=1
        return self.array[self.size]

    def resize(self) -> None:
        array_2 = [0] * len(self.array) * 2

        for i in range(len(self.array)):
            array_2[i] = self.array[i]
        self.array = array_2

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return len(self.array)
