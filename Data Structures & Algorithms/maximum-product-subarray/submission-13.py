class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curr_max , curr_min , global_max = nums[0] , nums[0] , nums[0]
        for i in range(1 , len(nums)):
            temp = curr_max
            curr_max = max(temp * nums[i] , curr_min * nums[i] , nums[i])
            curr_min = min(temp * nums[i] , curr_min * nums[i] , nums[i])
            global_max = max(global_max , curr_max)
        return global_max