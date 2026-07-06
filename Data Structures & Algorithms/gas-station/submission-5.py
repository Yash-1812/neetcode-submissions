class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            visited = set()
            total = 0
            j = i
            while j not in visited:
                total += gas[j] - cost[j]
                if total < 0:
                    break
                visited.add(j)
                if j == len(gas) - 1:
                    j = 0
                else:
                    j += 1
            if len(visited) == len(gas):
                return i
        return -1