class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        hold = -float('inf')
        sell = 0
        rest = 0
        for price in prices:
            prev_hold = hold
            prev_sell = sell
            prev_rest = rest
            hold = max(prev_hold , prev_rest - price)
            sell = prev_hold + price
            rest = max(prev_sell , prev_rest)
        return max(sell , rest)