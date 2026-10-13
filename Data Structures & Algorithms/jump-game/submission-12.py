class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if farthest == len(nums) - 1:
                return True
            if i > farthest:
                return False
            farthest = max(farthest , i + nums[i])
        return True