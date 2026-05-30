class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [0] * (n + 2)
        nums[0] = 0
        nums[1] = 1
        for i in range(2 , n + 2):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[n + 1]