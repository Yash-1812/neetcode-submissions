class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        part = []
        def backtrack(i , curr_target):
            if curr_target == target and i == len(nums):
                res.append(part.copy())
                return
            if curr_target > target or i >= len(nums):
                return
            part.append(nums[i])
            backtrack(i , curr_target + nums[i])
            part.pop()
            backtrack(i + 1 , curr_target)
        backtrack(0 , 0)
        return res