import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        for i in range(len(stones)):
            heapq.heappush(min_heap , -stones[i])
        while len(min_heap) > 1:
            x = -(heapq.heappop(min_heap))
            y = -(heapq.heappop(min_heap))
            if x == y:
                continue
            elif x < y:
                heapq.heappush(min_heap , -(y - x))
            elif y < x:
                heapq.heappush(min_heap , -(x - y))
        
        return -heapq.heappop(min_heap) if len(min_heap) > 0 else 0
