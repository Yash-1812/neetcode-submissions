class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visited = set()
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        def dfs(i , j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i , j) in visited:
                return True
            if board[i][j] == 'X':
                return True
            visited.add((i , j))
            up = dfs(i - 1 , j)
            down = dfs(i + 1 , j)
            left = dfs(i , j - 1)
            right = dfs(i , j + 1)
            return up and down and left and right 
            
        def clear():
            for i , j in visited:
                board[i][j] = 'X'

        for i in range(m):   #(int i = 0 ; i < m ; i ++)
            for j in range(n):
                if board[i][j] == 'O':
                    if dfs(i , j):
                        clear()
                    visited.clear()