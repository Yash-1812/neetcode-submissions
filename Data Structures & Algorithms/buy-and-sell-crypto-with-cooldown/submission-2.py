class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        holding = -float('inf')
        selling = 0
        resting = 0

        for price in prices:
            prev_holding = holding
            prev_selling = selling
            prev_resting = resting
            holding = max(prev_holding , prev_resting - price)
            selling = prev_holding + price
            resting = max(prev_resting , prev_selling)

        return max(resting ,selling)