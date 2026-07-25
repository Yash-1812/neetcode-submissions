class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        freq = Counter(nums)
        max_val = max(freq.values())
        return True if max_val > 1 else False