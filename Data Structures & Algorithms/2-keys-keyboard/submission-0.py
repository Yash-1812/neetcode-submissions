class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2 , n + 1):
            for j in range(i - 1 , 0 , -1):
                if i % j != 0:
                    continue
                else:
                    num = i // j
                    paste = num - 1
                    copy = 1
                    dp[i] = min(dp[i] , dp[j] + copy + paste)
        return dp[n]