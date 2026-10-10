class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        part = []
        def backtrack(i):
            if i == len(nums):
                res.append(part.copy())
                return
            part.append(nums[i])
            backtrack(i + 1)
            part.pop()
            backtrack(i + 1)
        backtrack(0)
        return res