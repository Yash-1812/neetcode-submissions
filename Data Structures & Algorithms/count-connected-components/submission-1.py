from collections import defaultdict , deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1

                queue = deque([i])
                visited.add(i)
                while queue:
                    node = queue.popleft()
                    for neighbours in graph[node]:
                        if neighbours not in visited:
                            visited.add(neighbours)
                            queue.append(neighbours)
        
        return count