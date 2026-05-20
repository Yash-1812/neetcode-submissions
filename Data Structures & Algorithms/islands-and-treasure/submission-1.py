from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()

        def addLand(r , c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == -1 or (r,c) in visited:
                return
            queue.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                grid[r][c] = dist
                addLand(r + 1 , c)
                addLand(r , c + 1)
                addLand(r - 1 , c)
                addLand(r , c - 1)
            dist += 1

