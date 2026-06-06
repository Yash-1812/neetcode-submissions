import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        count = 0
        max_heap = []
        for i in range(len(profits)):
            heapq.heappush(max_heap , (-profits[i] , capital[i]))
        temp = []
        while count < k:
            while max_heap and max_heap[0][1] > w:
                temp.append(heapq.heappop(max_heap))
            if not max_heap:
                break
            p , c = heapq.heappop(max_heap)
            w += -p
            while temp:
                price , cap = temp.pop(0)
                heapq.heappush(max_heap , (price , cap))
            count += 1
        return w
        