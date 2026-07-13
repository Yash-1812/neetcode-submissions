class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = x
        left , right = 0 , x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans