class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.res = 0
        def backtrack(curr_sum , idx):
            if idx == len(nums):
                if curr_sum == target:
                    self.res += 1
                return
            num = nums[idx]
            backtrack(curr_sum + num , idx + 1)
            backtrack(curr_sum - num , idx + 1)
        
        backtrack(0 , 0)
        return self.res