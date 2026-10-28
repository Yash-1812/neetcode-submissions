class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        part = []
        res = []
        nums.sort()
        def backtrack(idx):
            if tuple(part) in visited:
                return
            res.append(part.copy())
            visited.add(tuple(part))
            for i in range(idx , len(nums)):
                part.append(nums[i])
                backtrack(i + 1)
                part.pop()
        backtrack(0)
        return res