class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        parts = []
        res = []
        def backtrack(idx):
            res.append(parts.copy())
            for i in range(idx , len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                parts.append(nums[i])
                backtrack(i + 1)
                parts.pop()
        backtrack(0)
        return res