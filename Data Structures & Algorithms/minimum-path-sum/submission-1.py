class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(cols - 2 , -1 , -1):
            grid[rows - 1][i] += grid[rows - 1][i + 1]
        for i in range(rows - 2 , -1 , -1):
            grid[i][cols - 1] += grid[i + 1][cols - 1]
        
        for i in range(rows - 2 , -1 , -1):
            for j in range(cols - 2 , -1 , -1):
                grid[i][j] += min(grid[i+1][j] , grid[i][j+1])

        return grid[0][0]