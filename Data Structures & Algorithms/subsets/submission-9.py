class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        part = []
        def subset(part , i):
            if i == len(nums):
                res.append(part.copy())
                return
            part.append(nums[i])
            subset(part , i + 1)
            part.pop()
            subset(part , i + 1)
        subset(part , 0)
        return res