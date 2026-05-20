class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        s_ = 0
        for i in range(1 , len(nums) + 1):
            s_ = s_ + i
        return s_ - s