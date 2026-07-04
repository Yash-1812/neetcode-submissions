class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a , b in edges:
            graph[a].add(b)
            graph[b].add(a)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
        return count
