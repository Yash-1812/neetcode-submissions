class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy , max_profit = 0 , 0
        for i in range(1 , len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                max_profit = max(max_profit , prices[i] - prices[buy])

        return max_profit