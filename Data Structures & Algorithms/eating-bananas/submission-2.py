import math
class Solution:
    def calc_hours(self , k , piles):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile / k)
        return hrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            expected_hours = self.calc_hours(mid , piles)

            if expected_hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res