class Solution:
    def combinations(self , nums , idx , output , subset):
        if idx == len(nums):
            output.append(subset.copy())
            return

        subset.append(nums[idx])
        self.combinations(nums , idx + 1 , output , subset)
        subset.pop()
        self.combinations(nums , idx + 1 , output , subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        self.combinations(nums , 0 , output , [])
        return output