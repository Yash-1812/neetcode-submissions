import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap , -num)
        ele = 0
        for _ in range(k):
            ele = heapq.heappop(max_heap)
        return -ele