class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        part = []
        visited = set()
        def backtrack():
            if len(part) == len(nums):
                res.append(part.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                part.append(num)
                visited.add(num)
                backtrack()
                visited.remove(num)
                part.pop()
        backtrack()
        return res