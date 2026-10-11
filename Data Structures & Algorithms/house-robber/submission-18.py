class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        n = len(nums)
        nums[n - 2] = max(nums[n - 1] , nums[n - 2]) 
        for i in range(n - 3 , -1 , -1):
            nums[i] = max(nums[i + 1] , nums[i + 2] + nums[i])
        return nums[0]