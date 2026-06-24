class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        squares = [i*i for i in range(1 , n) if i*i <= n]
        nums = [n + 1] * (n + 1)
        nums[0] = 0
        for i in range(1 , n + 1):
            for sq in squares:
                if i - sq >= 0:
                    nums[i] = min(nums[i] , 1 + nums[i - sq])

        return nums[n]