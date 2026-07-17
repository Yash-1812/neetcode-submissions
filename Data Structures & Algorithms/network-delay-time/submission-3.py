class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(set)
        for u , v , w in times:
            graph[u].add((v , w))
        min_heap = [(0 , k)]
        visited = set()
        while min_heap:
            time , node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            for nei , w in graph[node]:
                new_time = time + w
                heapq.heappush(min_heap , (new_time , nei))
        return -1