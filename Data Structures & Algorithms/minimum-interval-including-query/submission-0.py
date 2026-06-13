class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        for q in queries:
            min_len = float('inf')
            for interval in intervals:
                if interval[0] <= q <= interval[1]:
                    min_len = min(min_len , interval[1] - interval[0] + 1)
            if min_len == float('inf'):
                output.append(-1)
            else:
                output.append(min_len)
        return output