class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        part = []
        nums.sort()
        visit = set()
        def backtrack():
            if len(part) == len(nums):
                if tuple(part) not in visit:
                    res.append(part.copy())
                    visit.add(tuple(part))
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