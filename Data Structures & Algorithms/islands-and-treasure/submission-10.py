class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i , j))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr , dc in directions:
                    nr , nc = r + dr , c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if grid[nr][nc] != 2 ** 31 - 1:
                        continue
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr , nc))