class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        parts = []
        visit = set()
        visited = set()
        def backtrack():
            if len(parts) == len(nums):
                if tuple(parts) not in visit:
                    res.append(parts.copy())
                    visit.add(tuple(parts))
                    return
                
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                parts.append(nums[i])
                backtrack()
                visited.remove(i)
                parts.pop()
        backtrack()
        return res