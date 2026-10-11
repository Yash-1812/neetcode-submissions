class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.perimeter = 0
        visited = set()
        def dfs(i , j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if grid[i][j] == 0:
                return 1
            if (i , j) in visited:
                return 0
            visited.add((i , j))
            a = dfs(i + 1 , j)
            b = dfs(i , j + 1)
            c = dfs(i - 1 , j)
            d = dfs(i , j - 1)
            return a + b + c + d
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i , j)