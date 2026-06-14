class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(rate):
            time = 0
            for p in piles:
                if p <= rate:
                    time += 1
                else:
                    if p % rate == 0:
                        time += p // rate
                    else:
                        time += (p // rate) + 1
            return time

        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if get_time(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left