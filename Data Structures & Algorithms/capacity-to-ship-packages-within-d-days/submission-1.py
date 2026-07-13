class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights) , sum(weights)
        def canShip(capacity):
            d = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > capacity:
                    curr_weight = w
                    d += 1
                else:
                    curr_weight += w
            return d <= days
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans