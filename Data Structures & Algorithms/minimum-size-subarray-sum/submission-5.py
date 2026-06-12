class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if len(nums) == 1 and target <= nums[0]:
            return 1
        if len(nums) == 1 and target > nums[0]:
            return 0
        if sum(nums) < target:
            return 0
        
        start , min_length = 0 , len(nums)
        for i in range(1 , len(nums)):
            if sum(nums[start:i]) >= target:
                while sum(nums[start:i]) >= target:
                    min_length = min(min_length , i - start)
                    start += 1
        n = len(nums)
        while sum(nums[start:n]) >= target:
            min_length = min(min_length , n - start)
            start += 1
        return min_length
        
