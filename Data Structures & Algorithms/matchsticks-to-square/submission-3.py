class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        length = sum(nums) // 4
        if sum(nums) % 4 != 0:
            return False
        nums.sort(reverse = True)
        sides = [0] * 4
        if nums[0] > length:
            return False
        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(4):
                if nums[i] + sides[j] <= length:
                    sides[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= nums[i]
            return False
        return backtrack(0)