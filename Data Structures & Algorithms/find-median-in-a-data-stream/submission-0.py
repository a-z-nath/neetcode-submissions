class MedianFinder:

    def __init__(self):
        self.arr = []
        self.l = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.l += 1

    def findMedian(self) -> float:
        self.arr.sort()
        
        if self.l % 2 == 1:
            return self.arr[self.l // 2]
        return (self.arr[self.l // 2] + self.arr[self.l // 2 - 1])/ 2