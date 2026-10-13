class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i] , 0)
        for c in count:
            heapq.heappush(max_heap , (-count[c] , c))
        i = 0
        output = []
        while i < k:
            _ , val = heapq.heappop(max_heap)
            output.append(val)
            i += 1
        return output