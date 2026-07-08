class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        part = []
        def backtrack(start):
            if len(part) == k:
                result.append(part.copy())
                return
            for i in range(start , n + 1):
                part.append(i)
                backtrack(i + 1)
                part.pop()
        backtrack(1)
        return result