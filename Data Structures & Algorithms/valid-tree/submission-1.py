from collections import defaultdict , deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        queue = deque([0])
        visited.add(0)

        while queue:
            node = queue.popleft()
            for neighbours in graph[node]:
                if neighbours not in visited:
                    visited.add(neighbours)
                    queue.append(neighbours)

        return len(visited) == n
        