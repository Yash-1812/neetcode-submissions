class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1 , n):
            x = dp[i]
            for j in range(i - 1 , -1 , -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i] , x + dp[j])
        return max(dp)