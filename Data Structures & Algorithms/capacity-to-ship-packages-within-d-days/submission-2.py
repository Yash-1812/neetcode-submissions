class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def find_days(cap):
            d = 0
            curr = 0
            for i in range(len(weights)):
                if curr + weights[i] > cap:
                    d += 1
                    curr = weights[i]
                else:
                    curr += weights[i]
            return d + 1

        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            d = find_days(mid)
            if d <= days:
                right = mid - 1
            elif d > days:
                left = mid + 1
        return left