class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i , j))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        minutes = -1
        if fresh == 0:
            return 0
        while queue:
            for _ in range(len(queue)):
                i , j = queue.popleft()
                for dr , dc in directions:
                    nr , nc = i + dr , j + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    fresh -= 1
                    queue.append((nr , nc))
                    grid[nr][nc] = 2
            minutes += 1
        return minutes if fresh == 0 else -1