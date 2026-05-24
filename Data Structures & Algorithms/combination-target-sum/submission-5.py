class Solution:
    def combinations(self , nums , target , idx , subset , output):
        if sum(subset) == target:
            output.append(subset.copy())
            return
        if idx == len(nums) or sum(subset) > target:
            return
        subset.append(nums[idx])
        self.combinations(nums , target , idx , subset , output)
        subset.pop()
        self.combinations(nums , target , idx + 1 , subset , output)
         
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        self.combinations(nums , target , 0 , [] , output)
        return output