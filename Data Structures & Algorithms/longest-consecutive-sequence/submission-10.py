class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap , n)
        res = 0
        visited = set()
        while min_heap:
            num = heapq.heappop(min_heap)
            if visited and num - 1 not in visited:
                res = max(len(visited) , res)
                visited.clear()
            visited.add(num)
        return max(res , len(visited))