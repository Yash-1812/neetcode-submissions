class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last = prices[0]
        profit = 0
        for i in range(1 , len(prices)):
            if prices[i] > last:
                profit += prices[i] - last
            last = prices[i]
        return profit
