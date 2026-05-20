class Solution:
    def getAnswer(self , result , nums , target , idx , subset):
        if target == 0 and subset not in result:
            result.append(subset.copy())
        if target < 0 or idx == len(nums):
            return

        subset.append(nums[idx])
        self.getAnswer(result , nums , target - nums[idx] , idx , subset)
        self.getAnswer(result , nums , target - nums[idx] , idx + 1 , subset)
        subset.pop()
        self.getAnswer(result , nums , target , idx + 1 , subset)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.getAnswer(result , nums , target , 0 , [])
        return result