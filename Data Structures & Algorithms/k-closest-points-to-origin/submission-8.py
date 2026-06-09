import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for a , b in points:
            dist = (a ** 2) + (b ** 2)
            heapq.heappush(min_heap , (dist , (a , b)))
        output = []
        for _ in range(k):
            copy = heapq.heappop(min_heap)
            output.append(copy[1])
        return output