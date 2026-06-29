class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
        left , right = 0 , 0
        min_len = len(nums)
        curr_sum = 0
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len , right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        return 0 if left == 0 else min_len