class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        total = [float('inf')] * (amount + 1)  # Total coins required to make ith amount
        total[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    total[i] = min(total[i] , total[i - coin] + 1)
        
        return total[amount] if total[amount] != float('inf') else -1