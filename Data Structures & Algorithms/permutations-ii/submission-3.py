class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        visit = set()
        visited = set()
        part = []
        def backtrack():
            if len(part) == len(nums):
                if tuple(part) in visit:
                    return
                result.append(part.copy())
                visit.add(tuple(part))
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                part.append(nums[i])
                visited.add(i)
                backtrack()
                part.pop()
                visited.remove(i)
        backtrack()
        return result