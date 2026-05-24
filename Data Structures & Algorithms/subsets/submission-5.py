class Solution:
    def combinations(self , nums , output , idx , subset):
        if idx == len(nums):
            output.append(subset.copy())
            return
        subset.append(nums[idx])
        self.combinations(nums , output , idx + 1 , subset)
        subset.pop()
        self.combinations(nums , output , idx + 1 , subset)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.combinations(nums , output , 0 , [])
        return output