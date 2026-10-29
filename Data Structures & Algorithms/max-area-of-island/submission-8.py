class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        visited = set()
        def dfs(i , j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if (i , j) in visited:
                return 0
            if grid[i][j] == 0:
                return 0
            visited.add((i , j))
            area = 1
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