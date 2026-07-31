class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        for p , c in zip(profits , capital):
            heapq.heappush(max_heap , (-p , c))
        while k > 0:
            stack = []
            while True:
                if not max_heap:
                    return w

                p , c = heapq.heappop(max_heap)
                if c > w:
                    stack.append((p , c))
                else:
                    w += (-p)
                    break
            while stack:
                heapq.heappush(max_heap , stack.pop())
            k -= 1
        return w