class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_recharge = 0
        target = len(nums) - 1
        for i in range(len(nums)):
            if i > max_recharge:
                return False
            max_recharge = max(max_recharge , i + nums[i])
        return True