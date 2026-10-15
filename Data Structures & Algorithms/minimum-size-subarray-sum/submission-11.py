class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        curr_sum = 0
        for i in range(0 , len(nums)):
            while curr_sum + nums[i] >= target:
                res = min(res , i - left + 1)
                curr_sum -= nums[left]
                left += 1
            curr_sum += nums[i]
        return res if res != float('inf') else 0