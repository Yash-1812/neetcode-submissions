class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
        for f in freq:
            if freq[f] > 1:
                return True
        return False