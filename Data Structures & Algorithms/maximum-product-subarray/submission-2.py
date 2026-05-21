class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        global_max , current_max , current_min = nums[0] , nums[0] , nums[0]

        for i in range(1 , len(nums)):

            options = (nums[i] , current_max * nums[i] , current_min * nums[i])
            current_max = max(options)
            current_min = min(options)

            global_max = max(current_max , global_max)

        return global_max