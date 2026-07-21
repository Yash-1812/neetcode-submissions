class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.res = 0
        def backtrack(curr_target , idx):
            if curr_target == target and idx == len(nums):
                self.res += 1
                return
            if idx == len(nums):
                return 
            backtrack(curr_target + nums[idx] , idx + 1)
            backtrack(curr_target - nums[idx] , idx + 1)
        backtrack(0 , 0)
        return self.res