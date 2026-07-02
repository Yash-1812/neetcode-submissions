class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap , num)
        output = 0
        length = 0
        while min_heap:
            num = heapq.heappop(min_heap)
            if min_heap and ((min_heap[0] - num) == 1):
                length += 1
            if min_heap and ((min_heap[0] - num) > 1):
                output = max(output , length + 1)
                length = 0
            
        return max(output , length + 1)