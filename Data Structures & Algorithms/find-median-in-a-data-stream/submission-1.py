class MedianFinder:

    def __init__(self):
        # two heap, large -> minHeap, small -> maxHeap
        # two heaps with equal size
        self.large, self.small = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        # maintain size
        if len(self.small) > len(self.large) + 1:
            num = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        if len(self.large) > len(self.small) + 1:
            num = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, num)

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] + -1 * self.small[0]) / 2
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -1 * self.small[0]