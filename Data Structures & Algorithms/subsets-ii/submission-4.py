class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        part = []
        visited = set()
        def backtrack(i):
            if i == len(nums):
                if tuple(part) in visited:
                    return
                result.append(part.copy())
                visited.add(tuple(part))
                return
            part.append(nums[i])
            backtrack(i + 1)
            part.pop()
            backtrack(i + 1)
        backtrack(0)
        return result