import math
class Solution:

    def calc_hours(self , k_val , piles):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile / k_val)
        return hrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k_array = [i for i in range(1 , max(piles) + 1)]
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