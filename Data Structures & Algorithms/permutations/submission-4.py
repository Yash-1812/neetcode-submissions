class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        parts = []
        visited = set()
        def backtrack(idx):
            if len(parts) == len(nums):
                result.append(parts.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                parts.append(nums[i])
                visited.add(i)
                backtrack(i + 1)
                parts.pop()
                visited.remove(i)
        backtrack(0)
        return result