class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(set)
        for u , v , w in times:
            graph[u].add((v , w))
        visited = set()
        min_heap = [(0 , k)]
        while min_heap:
            time , node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            for nei , w in graph[node]:
                if nei not in visited:
                    t = time + w
                    heapq.heappush(min_heap , (t , nei))
        return -1