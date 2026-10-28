class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        part = []
        def backtrack(idx , curr_target):
            if curr_target == 0:
                res.append(part.copy())
                return
            if curr_target < 0 or idx >= len(nums):
                return
            part.append(nums[idx])
            backtrack(idx , curr_target - nums[idx])
            part.pop()
            backtrack(idx + 1 , curr_target)
        backtrack(0 , target)
        return res 