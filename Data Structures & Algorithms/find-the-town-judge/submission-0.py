class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_scores = [0] * (n + 1)

        for a , b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for persons in range(1 , n + 1):
            if trust_scores[persons] == n - 1:
                return persons

        return -1