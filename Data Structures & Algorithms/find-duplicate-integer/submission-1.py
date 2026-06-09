class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visit = set()
        for num in nums:
            if num in visit:
                return num
            visit.add(num)
        