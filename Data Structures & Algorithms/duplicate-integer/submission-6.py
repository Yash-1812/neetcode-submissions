class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False