class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i , 0)
        return min(freq , key = freq.get)