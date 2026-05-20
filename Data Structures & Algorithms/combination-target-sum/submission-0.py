class Solution:
    def getAnswer(self , nums , idx , result , subset , target):
       
        if sum(subset) > target:
            return
        if sum(subset) == target:
            if subset not in result:
                result.append(subset.copy())
            return
        if idx < len(nums):
            subset.append(nums[idx])
            self.getAnswer(nums , idx + 1 , result , subset , target)
            self.getAnswer(nums , idx , result , subset , target)
            subset.pop()
            self.getAnswer(nums , idx + 1 , result , subset , target)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.getAnswer(nums , 0 , result , [] , target)
        return result