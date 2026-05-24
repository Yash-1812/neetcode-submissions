class Solution:
    def combinations(self , nums , target , output , subset , idx):
        if sum(subset) == target:
            output.append(subset.copy())
            return
        if sum(subset) > target or idx == len(nums):
            return
        subset.append(nums[idx])
        self.combinations(nums , target , output , subset , idx)
        subset.pop()
        self.combinations(nums , target , output , subset , idx + 1)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []
        self.combinations(nums , target , output , [] , 0)
        return output