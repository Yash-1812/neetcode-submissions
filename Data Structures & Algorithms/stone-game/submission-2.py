class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def backtrack(i , j):
            if i == j:
                return piles[i]
            if (i , j) in memo:
                return memo[(i , j)]
            pick_left = piles[i] - backtrack(i + 1 , j)
            pick_right = piles[j] - backtrack(i , j - 1)
            memo[(i , j)] =  max(pick_left , pick_right)
            return memo[(i , j)]
        return backtrack(0 , len(piles) - 1) > 0