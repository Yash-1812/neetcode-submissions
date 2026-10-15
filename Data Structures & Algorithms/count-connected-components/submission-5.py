class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = collections.defaultdict(set)
        for a , b in edges:
            graph[a].add(b)
            graph[b].add(a)
        res = 0
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            res += 1
            queue = deque([i])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei in visited:
                            continue
                        queue.append(nei)
                        visited.add(nei)
        return res