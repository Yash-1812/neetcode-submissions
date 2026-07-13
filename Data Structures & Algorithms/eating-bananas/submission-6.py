class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(rate):
            hours = 0
            for p in piles:
                if p % rate == 0:
                    hours += p // rate
                else:
                    hours += (p // rate) + 1
            return hours

        left , right = 1 , max(piles)
        ans = 1
        while left <= right:
            rate = (left + right) // 2
            hours = get_hours(rate)
            if hours <= h:
                ans = rate
                right = rate - 1
            else:
                left = rate + 1
        return ans