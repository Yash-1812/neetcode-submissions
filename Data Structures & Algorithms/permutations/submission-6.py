class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        parts = []
        res = []
        visited = set()
        def backtrack():
            if len(parts) == len(nums):
                res.append(parts.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                parts.append(nums[i])
                backtrack()
                visited.remove(i)
                parts.pop()
        backtrack()
        return res