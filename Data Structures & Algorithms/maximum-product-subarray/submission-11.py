class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        global_max , current_max , current_min = nums[0] , nums[0] , nums[0]
        for i in range(1 , len(nums)):
            temp = current_max
            current_max = max(nums[i] , temp*nums[i] , current_min*nums[i])
            current_min = min(nums[i] , temp*nums[i] , nums[i]*current_min)

            global_max = max(global_max , current_max)
        return global_max