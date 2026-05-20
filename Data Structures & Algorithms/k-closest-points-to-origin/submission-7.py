import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x , y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(min_heap , (dist , [x , y]))
        result = []
        while k > 0:
            dist , points = heapq.heappop(min_heap)
            result.append(points)
            k -= 1
        return result



        