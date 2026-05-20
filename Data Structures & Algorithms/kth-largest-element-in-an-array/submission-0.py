import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap , -nums[i])
        for _ in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)