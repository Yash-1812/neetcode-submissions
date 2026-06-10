class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = -float('inf')
        curr_sum , max_sum = nums[0] , nums[0]
        for i in range(1 , len(nums)):
            curr_sum = max(nums[i] , curr_sum + nums[i])
            max_sum = max(max_sum , curr_sum)
        global_max = max(global_max , max_sum)
        s = sum(nums)
        min_sum , curr_min = nums[0] , nums[0]
        for i in range(1 , len(nums)):
            curr_min = min(nums[i] , nums[i] + curr_min)
            min_sum = min(min_sum , curr_min)
        return global_max if max_sum < 0 else max(global_max , s - min_sum)