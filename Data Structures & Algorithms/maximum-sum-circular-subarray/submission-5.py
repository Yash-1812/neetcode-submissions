class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max , global_max = nums[0] , nums[0]
        for i in range(1 , len(nums)):
            curr_max = max(nums[i] , curr_max + nums[i])
            global_max = max(global_max , curr_max)
        s = sum(nums)
        curr_min , global_min = nums[0] , nums[0]
        for i in range(1 , len(nums)):
            curr_min = min(nums[i] , curr_min + nums[i])
            global_min = min(global_min , curr_min)
        return global_max if global_max < 0 else max(global_max , s - global_min)