class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if cost[i] > gas[i]:
                continue
            j = i
            total = 0
            visited = set()
            while total >= 0 and j not in visited:
                total += gas[j] - cost[j]
                visited.add(j)
                if j == len(gas) - 1:
                    j = 0
                else:
                    j += 1
            if len(visited) == len(gas) and total >= 0:
                return i
        return -1