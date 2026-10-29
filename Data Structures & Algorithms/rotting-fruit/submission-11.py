class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i , j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = -1
        directions = [(1,0) , (0,-1) , (0,1) , (-1,0)]
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr , dc in directions:
                    nr , nc = dr + r , dc + c
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr , nc))
            minutes += 1
        return minutes if fresh == 0 else -1