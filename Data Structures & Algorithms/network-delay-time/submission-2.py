class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(set)
        for u , v , w in times:
            adj_list[u].add((v , w))
        min_heap = [(0 , k)]
        visited = set()
        while min_heap:
            time , node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            for nei , weight in adj_list[node]:
                if nei not in visited:
                    new_weight = weight + time
                    heapq.heappush(min_heap , (new_weight , nei))
        return -1