class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_size = float('inf')
        current_sum = 0

        for end in range(len(nums)):
            current_sum += nums[end]

            while current_sum >= target:
                min_size = min(min_size , end - start + 1)
                current_sum -= nums[start]
                start += 1
        
        return min_size if min_size != float('inf') else 0