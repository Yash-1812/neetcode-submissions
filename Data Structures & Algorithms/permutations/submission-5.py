class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        part = []
        def backtrack():
            if len(part) == len(nums):
                res.append(part.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                part.append(nums[i])
                backtrack()
                visited.remove(i)
                part.pop()
        backtrack()
        return res