class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nums[n - 2] = max(nums[n - 1] , nums[n - 2])
        for i in range(n - 3 , -1 , -1):
            nums[i] = max(nums[i] + nums[i + 2] , nums[i + 1])
        return nums[0]