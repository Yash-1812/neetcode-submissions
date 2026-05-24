class Solution:
    def combinations(self , nums , idx , subset , output):
        if idx == len(nums):
            output.append(subset.copy())
            return

        subset.append(nums[idx])
        self.combinations(nums , idx + 1 , subset , output)
        subset.pop()
        self.combinations(nums , idx + 1 , subset , output)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        self.combinations(nums , 0 , [] , output)
        return output