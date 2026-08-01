class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(i , j):
            if i == j:
                return piles[i]
            if (i , j) in memo:
                return memo[(i , j)]
            pick_left = piles[i] + dp(i + 1 , j)
            pick_right = piles[j] + dp(i , j - 1)
            memo[(i , j)] = max(pick_left , pick_right)
            return memo[(i , j)]
        return dp(0 , len(piles) - 1) > 0