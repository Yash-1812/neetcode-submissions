class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        parts = []
        def backtrack(idx):
            if idx == len(nums):
                res.append(parts.copy())
                return
            parts.append(nums[idx])
            backtrack(idx + 1)
            parts.pop()
            backtrack(idx + 1)
        backtrack(0)
        return res