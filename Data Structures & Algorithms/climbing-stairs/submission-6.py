class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[n] , nums[n - 1] = 1 , 1
        if n == 1:
            return 1
        for i in range(n - 2 , -1 , -1):
            nums[i] = nums[i + 1] + nums[i + 2]
        return nums[0]