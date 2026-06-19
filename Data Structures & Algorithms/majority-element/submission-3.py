class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
        max_freq , max_freq_ele = 0 , 0
        for f in freq:
            if freq[f] > max_freq:
                max_freq = freq[f]
                max_freq_ele = f
        return max_freq_ele