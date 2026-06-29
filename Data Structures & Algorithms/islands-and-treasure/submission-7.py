class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i , j])
                    visited.add((i , j))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        dist = 0
        while queue:
            dist += 1
            n = len(queue)
            for _ in range(n):
                dr , dc = queue.popleft()
                for i , j in directions:
                    nr , nc = dr + i , dc + j
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr , nc) in visited:
                        continue
                    if grid[nr][nc] == -1:
                        continue
                    visited.add((nr , nc))
                    grid[nr][nc] = dist
                    queue.append([nr , nc])
        
