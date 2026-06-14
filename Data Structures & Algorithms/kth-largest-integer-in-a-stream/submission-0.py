import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxH = []
        self.c = k
        for num in nums:
            heapq.heappush(self.maxH , -num)
    def add(self, val: int) -> int:
        heapq.heappush(self.maxH , -val)
        temp = []
        for _ in range(self.c):
            temp.append(heapq.heappop(self.maxH))
        ans = temp[-1]
        for t in temp:
            heapq.heappush(self.maxH , t)
        return -ans
        
