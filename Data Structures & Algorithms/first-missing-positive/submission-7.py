class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set()
        for i in range(len(nums)):
            num_set.add(nums[i])
        #min_val = min(nums)
        max_val = max(nums)
        result = float('inf')
        for i in range(1 , 2**31 + 1):
            if i not in num_set:
                result = i
                break
        return max_val + 1 if result == float('inf') else result