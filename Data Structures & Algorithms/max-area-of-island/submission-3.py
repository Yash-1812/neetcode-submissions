class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i , j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            current_area = 1
            current_area += dfs(i + 1 , j)
            current_area += dfs(i , j + 1)
            current_area += dfs(i , j - 1)
            current_area += dfs(i - 1 , j)

            return current_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r , c)
                    max_area = max(max_area , area)
        
        return max_area

