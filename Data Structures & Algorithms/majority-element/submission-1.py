from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        max_freq = 0
        output = -1
        for num in nums:
            if freq[num] > max_freq:
                max_freq = freq[num]
                output = num
        return output