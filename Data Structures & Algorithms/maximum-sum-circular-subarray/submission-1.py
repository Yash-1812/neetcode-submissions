class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = nums[0]
        global_min = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        total = sum(nums)
        for i in range(1 , len(nums)):
            current_max = max(nums[i] , current_max + nums[i])
            global_max = max(current_max , global_max)

            current_min = min(nums[i] , current_min + nums[i])
            global_min = min(current_min , global_min)

        if global_max < 0:
            return global_max
        
        return global_max if (global_max > total - global_min) else total - global_min