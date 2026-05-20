class Solution:
    def getSubsets(self , result , nums , idx , subset):
        if idx == len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[idx])
        self.getSubsets(result , nums , idx + 1 , subset)
        subset.pop()
        self.getSubsets(result , nums , idx + 1 , subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.getSubsets(result , nums , 0 , [])
        return result