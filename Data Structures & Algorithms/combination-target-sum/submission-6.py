class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        part = []
        res = []
        def backtrack(curr_target , idx):
            if curr_target == 0:
                res.append(part.copy())
                return
            if curr_target < 0 or idx >= len(nums):
                return
            part.append(nums[idx])
            backtrack(curr_target - nums[idx] , idx)
            part.pop()
            backtrack(curr_target , idx + 1)
        backtrack(target , 0)
        return res