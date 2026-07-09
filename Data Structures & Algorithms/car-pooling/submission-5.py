class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        min_heap = []
        curr_pass = 0
        for i in range(0 , len(trips)):
            num_Pass , start , end = trips[i]
            while min_heap and start >= min_heap[0][0]:
                _ , p = heapq.heappop(min_heap)
                curr_pass -= p
            curr_pass += num_Pass
            if curr_pass > capacity:
                return False
            heapq.heappush(min_heap , (end , curr_pass))
        return True
