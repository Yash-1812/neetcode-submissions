class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        for p , c in zip(profits , capital):
            heapq.heappush(max_heap , (-p , c))
        stack = []
        for _ in range(k):
            if w >= max_heap[0][1]:
                prof , cap = heapq.heappop(max_heap)
                prof = -prof
                w += prof
            else:
                while max_heap and w < max_heap[0][1]:
                    stack.append(heapq.heappop(max_heap))
                if len(max_heap) == 0:return w
                prof , cap = heapq.heappop(max_heap)
                prof = -prof
                w += prof
            while stack:
                heapq.heappush(max_heap , stack.pop())
        return w