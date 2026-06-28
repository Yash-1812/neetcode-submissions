class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_len = 0
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        memo = {}
        def dfs(i , j):
            if (i , j) in memo:
                return memo[(i , j)]
            longest_path = 1
            for r , c in directions:
                nr , nc = r + i , c + j
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if matrix[nr][nc] <= matrix[i][j]:
                    continue
                longest_path = max(longest_path , 1 + dfs(nr , nc))
            memo[(i , j)] = longest_path
            return longest_path

        for i in range(rows):
            for j in range(cols):
                max_len = max(max_len , dfs(i , j))
        return max_len