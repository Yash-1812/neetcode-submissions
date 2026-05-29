class Solution:
    def tribonacci(self, n: int) -> int:
        nums = []
        nums.append(0)
        nums.append(1)
        nums.append(1)
        i = 3
        while i <= n:
            nums.append(nums[i - 1] + nums[i - 2] + nums[i - 3])
            i += 1
        return nums[n]