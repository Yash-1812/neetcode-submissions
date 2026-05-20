class Solution:
    def getAnswer(self , nums , target , idx , subset , result):
        if target == 0:
            if subset not in result:
                result.append(subset.copy())
            return
        if target < 0 or idx == len(nums):
            return
        subset.append(nums[idx])
        self.getAnswer(nums , target - nums[idx] , idx , subset , result)
        self.getAnswer(nums , target - nums[idx] , idx + 1 , subset , result)
        subset.pop()
        self.getAnswer(nums , target , idx + 1 , subset , result)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.getAnswer(nums , target , 0 , [] , result)
        return result
