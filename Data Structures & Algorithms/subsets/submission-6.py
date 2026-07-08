class Solution:
    def subset(self , nums , idx , part , result):
        if idx == len(nums):
            result.append(part.copy())
            return
        part.append(nums[idx])
        self.subset(nums , idx + 1 , part , result)
        part.pop()
        self.subset(nums , idx + 1 , part , result)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.subset(nums , 0 , [] , result)
        return result