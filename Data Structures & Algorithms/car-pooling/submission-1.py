class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        minheap = []
        curr_pass = 0
        for t in trips:
            while minheap and minheap[0][0] <= t[1]:
                curr_pass -= minheap[0][1]
                heapq.heappop(minheap)

            curr_pass += t[0]
            if curr_pass > capacity:
                return False
            heapq.heappush(minheap , [t[2] , t[0]])
        return True 