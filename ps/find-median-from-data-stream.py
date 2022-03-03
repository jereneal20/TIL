from heapq import *


class MedianFinder:

    def __init__(self):
        self.minheap = [10000000]
        self.maxheap = [10000000]  # store lower than median

    def addNum(self, num: int) -> None:
        val = num
        if val < -self.maxheap[0]:
            heappush(self.maxheap, -val)
        else:  # if val > minheap[0]:
            heappush(self.minheap, val)

        if len(self.minheap) > len(self.maxheap):
            tmp = heappop(self.minheap)
            heappush(self.maxheap, -tmp)
        elif len(self.minheap) < len(self.maxheap):
            tmp = -heappop(self.maxheap)
            heappush(self.minheap, tmp)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()