import collections
from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for i in range(len(bombs)):
            x , y , r = bombs[i]
            for j in range(len(bombs)):
                if i != j:
                    x_ , y_ , r_ = bombs[j]
                    dist = ((x - x_) ** 2 + (y - y_) ** 2) ** 0.5
                    if dist <= r:
                        graph[i].add(j)
        if not graph:
            return 1
        max_bombs = 1
        for i in range(len(bombs)):
            queue = deque([i])
            visited = set()
            visited.add(i)
            while queue:
                for _ in range(len(queue)):
                    bomb = queue.popleft()
                    for nei in graph[bomb]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            max_bombs = max(max_bombs , len(visited))
        return max_bombs