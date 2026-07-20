class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        min_heap = []
        total = 0
        for i in range(len(trips)):
            numPass , f , t = trips[i]
            while min_heap and f >= min_heap[0][0]:
                to , cap = heapq.heappop(min_heap)
                total -= cap
            total += numPass
            heapq.heappush(min_heap , (t , numPass))
            if total > capacity:
                return False
        return True