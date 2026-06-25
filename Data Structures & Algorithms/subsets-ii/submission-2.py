class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        freq = []
        def getsubset(nums , idx , subset):
            if idx == len(nums) and Counter(subset) not in freq:
                freq.append(Counter(subset))
                result.append(subset.copy())
                return
            if idx >= len(nums):
                return
            subset.append(nums[idx])
            getsubset(nums , idx + 1 , subset)
            subset.pop()
            getsubset(nums , idx + 1 , subset)
        
        getsubset(nums , 0 , [])
        return result