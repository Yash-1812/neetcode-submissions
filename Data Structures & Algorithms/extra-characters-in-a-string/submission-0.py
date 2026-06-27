class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        n = len(s)
        words = set(dictionary)
        dp = [0] * (n + 1)
        for i in range(1 , n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                substring = s[j:i]
                if substring in words:
                    dp[i] = min(dp[i] , dp[j])
        return dp[n]