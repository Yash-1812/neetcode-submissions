class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1:
            return 1 if obstacleGrid[m - 1][n - 1] == 0 else 0
        obstacle = False
        for i in range(n - 2 , -1 , -1):
            if obstacle == True:
                obstacleGrid[m - 1][i] = 0
            elif obstacleGrid[m - 1][i] == 1:
                obstacle = True
                obstacleGrid[m - 1][i] = 0
            else:
                obstacleGrid[m - 1][i] = 1
        obstacle = False
        for i in range(m - 2 , -1 , -1):
            if obstacle == True:
                obstacleGrid[i][n - 1] = 0
            elif obstacleGrid[i][n - 1] == 1:
                obstacle = True
                obstacleGrid[i][n - 1] = 0
            else:
                obstacleGrid[i][n - 1] = 1
        for i in range(m - 2 , -1 , -1):
            for j in range(n - 2 , -1 , -1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i + 1][j] + obstacleGrid[i][j + 1]
        return obstacleGrid[0][0]