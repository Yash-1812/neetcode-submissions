class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i , j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        minutes = -1
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                dr , dc = queue.popleft()
                for i , j in directions:
                    nr , nc = dr + i , dc + j
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr , nc))
        return minutes if fresh == 0 else -1
                    