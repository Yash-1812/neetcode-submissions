class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        n = len(isConnected[0])
        graph = collections.defaultdict(set)
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].add(j)
                    graph[j].add(i)
        visited = set()
        provinces = 0
        for i in range(m):
            if i in visited:
                continue
            visited.add(i)
            provinces += 1
            queue = deque([i])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei in visited:
                            continue
                        visited.add(nei)
                        queue.append(nei)
        return provinces