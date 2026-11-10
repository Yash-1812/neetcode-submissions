class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time(time):
            t = 0
            for p in piles:
                if p % time == 0:
                    t += (p // time)
                else:
                    t += (p // time) + 1
            return t
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            time_req = get_time(mid)
            if time_req > h:
                left = mid + 1
            else:
                right = mid - 1
        return left