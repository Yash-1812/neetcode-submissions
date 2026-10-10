class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        part = []
        def backtrack(num):
            if len(part) == k:
                res.append(part.copy())
                return
            if num > n:
                return
            for i in range(num , n + 1):
                part.append(i)
                backtrack(i + 1)
                part.pop()
        backtrack(1)
        return res