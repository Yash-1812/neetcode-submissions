class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        arr = [0] * (n + 1)
        for a , b in trust:
            arr[b] += 1
            arr[a] -= 1
        res = []
        for i in range(1 , len(arr)):
            if arr[i] == n - 1:
                res.append(i)
        return res[0] if len(res) == 1 else -1