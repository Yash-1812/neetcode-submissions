from functools import reduce
import operator
class Solution:
    def subsets(self, nums , idx , subset):
        if idx == len(nums):
            self.result += reduce(operator.xor, subset , 0)
            return
        subset.append(nums[idx])
        self.subsets(nums , idx + 1 , subset)
        subset.pop()
        self.subsets(nums , idx + 1 , subset)

    def subsetXORSum(self, nums: List[int]) -> int:
        self.result = 0
        self.subsets(nums , 0 , [])
        return self.result