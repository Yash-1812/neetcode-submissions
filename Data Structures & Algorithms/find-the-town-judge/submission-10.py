class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        arr = [0] * (n + 1)
        for a , b in trust:
            arr[b] += 1
            arr[a] -= 1
        count = 0
        ans = -1
        for i in range(len(arr)):
            if arr[i] == n - 1:
                return i
        return -1