class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_max , global_max , current_min = nums[0] , nums[0] , nums[0]
        for i in range(1 , len(nums)):
            num = nums[i]
            temp = current_max
            current_max = max(num , num * temp , num * current_min)
            current_min = min(num , num * temp , num * current_min)
            global_max = max(current_max , global_max)
        return global_max