class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        current_max , current_min , global_max = nums[0] , nums[0] , nums[0]
        for i in range(1 , len(nums)):
            temp = current_max
            current_max = max(nums[i] , temp * nums[i] , current_min * nums[i])
            current_min = min(nums[i] , temp * nums[i] , current_min * nums[i])
            global_max = max(global_max , current_max)
        return global_max