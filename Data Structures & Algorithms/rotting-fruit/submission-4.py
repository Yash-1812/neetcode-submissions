class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        
        queue = []
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        rotten = 0
        def infect(r , c , rotten , fresh):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or grid[r][c] == 2:
                return
            grid[r][c] = 2
            rotten += 1
            fresh -= 1
            queue.append([r , c])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i , j])
                    rotten += 1
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        t = -1
        while queue:
            for _ in range(len(queue)):
                r , c = queue.pop(0)
                infect(r + 1 , c , rotten , fresh)
                infect(r - 1 , c , rotten , fresh)
                infect(r , c + 1 , rotten , fresh)
                infect(r , c - 1 , rotten , fresh)
            t += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return -1 if fresh == 0 else t