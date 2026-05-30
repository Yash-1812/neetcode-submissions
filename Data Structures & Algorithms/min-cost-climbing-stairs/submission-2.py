class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        result = [0] * (n + 1)
        result[n] = 0
        result[n - 1] = cost[n - 1]
        for i in range(n - 2 , -1 , -1):
            result[i] = cost[i] + min(result[i + 1] , result[i + 2])
        return min(result[0] , result[1])