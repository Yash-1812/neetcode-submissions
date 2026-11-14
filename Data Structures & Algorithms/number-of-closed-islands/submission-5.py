import collections
from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        closed = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def is_closed(i , j):
            queue = deque([(i , j)])
            visited.add((i , j))
            is_island_closed = True
            while queue:
                for _ in range(len(queue)):
                    r , c = queue.popleft()
                    for dr , dc in directions:
                        nr , nc = dr + r , dc + c
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            is_island_closed = False
                            continue
                        if grid[nr][nc] == 1 or (nr , nc) in visited:
                            continue
                        visited.add((nr , nc))
                        queue.append((nr , nc))
            return is_island_closed
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i , j) not in visited:
                    if is_closed(i , j):
                        closed += 1
        return closed