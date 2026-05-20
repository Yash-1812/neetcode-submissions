class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i] , 0)
        max_key = max(freq, key=freq.get)
        return max_key