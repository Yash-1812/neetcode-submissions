class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        max_rob = max(nums[n - 1] , nums[n - 2])
        for i in range(n - 3 , -1 , -1):
            nums[i] = max(nums[i + 1] , nums[i + 2] + nums[i])
            max_rob = max(nums[i] , nums[i + 1])
        return max_rob