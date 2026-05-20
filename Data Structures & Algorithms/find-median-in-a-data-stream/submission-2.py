import heapq
class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        n = len(self.array)
        arr = sorted(self.array)
        return arr[n//2] if n % 2 != 0 else ((arr[n//2] + arr[(n//2) - 1]) / 2)
        