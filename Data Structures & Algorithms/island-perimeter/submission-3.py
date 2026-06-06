class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i , j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 1
            if grid[i][j] == 0:
                return 1
            if (i , j) in visit:
                return 0
            visit.add((i , j))
            perimeter = 0
            perimeter += dfs(i + 1 , j)
            perimeter += dfs(i , j + 1)
            perimeter += dfs(i - 1 , j)
            perimeter += dfs(i , j - 1)
            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i , j)
