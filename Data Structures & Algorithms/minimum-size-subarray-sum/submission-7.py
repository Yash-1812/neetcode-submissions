class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
        left , right = 0 , 1
        min_len = len(nums)
        while right <= len(nums):
            while sum(nums[left:right]) >= target:
                min_len = min(min_len , right - left)
                left += 1
            right += 1
        return 0 if left == 0 else min_len