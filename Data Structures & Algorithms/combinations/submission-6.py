class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        parts = []
        def backtrack(num):
            if len(parts) == k:
                res.append(parts.copy())
                return
            for i in range(num , n + 1):
                parts.append(i)
                backtrack(i + 1)
                parts.pop()
        backtrack(1)
        return res