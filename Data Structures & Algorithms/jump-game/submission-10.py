class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i in range(len(nums)):
            if max_jump == len(nums) - 1:
                return True
            if i > max_jump:
                return False
            max_jump = max(max_jump , i + nums[i])
        return True