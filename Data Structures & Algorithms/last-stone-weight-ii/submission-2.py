class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for w in range(target , stone - 1 , -1):
                if dp[w - stone]:
                    dp[w] = True
        for i in range(target , -1 , -1):
            if dp[i]:
                return total - 2 * i
        return 0
