class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_days(rate):
            days = 0
            for i in range(len(piles)):
                if piles[i] % rate == 0:
                    days += (piles[i]) // rate
                else:
                    days += ((piles[i]) // rate) + 1
            return days
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            days = find_days(mid)
            if days > h:
                left = mid + 1
            elif days <= h:
                right = mid - 1
        return left 