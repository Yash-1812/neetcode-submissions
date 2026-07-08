class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def dfs(i , j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
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

        def clear(visited):
            for i , j in visited:
                board[i][j] = 'X'

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if dfs(i , j):
                        clear(visited)
                    visited.clear()
            