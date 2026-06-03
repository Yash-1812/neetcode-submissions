class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue
            else:
                idx = i
                total = gas[i] - cost[i]
                i += 1
                while i % len(gas) != idx and total >= 0:
                    i_ = i % len(gas)
                    total += gas[i_] - cost[i_]
                    i += 1
                if total < 0: continue
                i_ = i % len(gas)
                total += gas[i_] - cost[i_]
                if i - len(gas) == idx and total >= 0:
                    return idx
        
        return -1