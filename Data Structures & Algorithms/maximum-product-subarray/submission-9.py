class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        current_max , global_max , current_min = nums[0] , nums[0] , nums[0]
        for i in range(1 , len(nums)):
            num = nums[i]
            temp = current_max
            current_max = max(temp*num , num , current_min*num)
            current_min = min(temp*num , num , current_min*num)
            global_max = max(current_max , global_max)

        return global_max