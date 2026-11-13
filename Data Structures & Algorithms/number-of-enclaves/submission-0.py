class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if grid[i][j] == 1:
                        queue.append((i , j))
                        grid[i][j] = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr , dc in directions:
                    nr , nc = r + dr , c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    queue.append((nr , nc))
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
        return res