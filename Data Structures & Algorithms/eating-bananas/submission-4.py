class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        def get_rate(piles , k):
            count = 0
            for p in piles:
                if p <= k:
                    count += 1
                else:
                    if p % k == 0:
                        count += (p // k)
                    else:
                        count += (p // k) + 1
            return count

        while left <= right:
            mid = (left + right) // 2
            rate = get_rate(piles , mid)
            if rate <= h:
                right = mid - 1
            elif rate > h:
                left = mid + 1
        return left


