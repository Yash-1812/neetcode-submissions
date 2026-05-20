class Solution:
    def sets(self , nums , idx , result , subset):
        if idx == len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[idx])
        self.sets(nums , idx + 1 , result , subset)
        subset.pop()
        self.sets(nums , idx + 1 , result , subset)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.sets(nums , 0 , result , [])
        return result