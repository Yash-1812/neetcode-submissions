class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i , j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:return 0
        minutes = -1
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        while queue:
            for _ in range(len(queue)):
                dr , dc = queue.pop(0)
                for i , j in directions:
                    nr , nc = dr + i , dc + j
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr , nc))
            minutes += 1
        return minutes if fresh == 0 else -1


        