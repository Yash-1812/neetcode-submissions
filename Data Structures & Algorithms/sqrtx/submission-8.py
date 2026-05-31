class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            sq_next = (mid + 1) * (mid + 1)
            if sq < x < sq_next:
                return mid 
            elif sq < x:
                left = mid + 1
            elif sq > x:
                right = mid - 1
            elif sq == x:
                return mid