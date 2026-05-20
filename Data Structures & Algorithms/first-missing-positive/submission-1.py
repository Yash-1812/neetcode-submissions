class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                num_set.add(nums[i])
        
        for i in range(1 , (2 ** 31) - 1):
            if i not in num_set:
                return i