class Solution:
    def climbStairs(self, n: int) -> int:
        nums = []
        nums.append(0)
        nums.append(1)
        for i in range(n):
            nums.append(nums[i] + nums[i + 1])
        return nums[n+1]