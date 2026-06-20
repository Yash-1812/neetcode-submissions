class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda t : t[1])
        curr_pass = 0
        min_heap = []
        for numPass , start , end in trips:
            while min_heap and min_heap[0][0] <= start:
                curr_pass -= heapq.heappop(min_heap)[1]
            curr_pass += numPass
            if curr_pass > capacity:
                return False
            heapq.heappush(min_heap , [end , numPass])
        return True 