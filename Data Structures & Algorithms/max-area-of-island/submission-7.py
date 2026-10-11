class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        def dfs(i , j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            area += dfs(i + 1 , j)
            area += dfs(i , j + 1)
            area += dfs(i , j - 1)
            area += dfs(i - 1 , j)
            return area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area , dfs(i , j))
        return max_area