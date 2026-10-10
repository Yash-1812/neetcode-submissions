class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def dfs(i , j , curr):
            if curr == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if board[i][j] != word[curr]:
                return False
            if (i , j) in visited:
                return False
            visited.add((i , j))
            up = dfs(i - 1 , j , curr + 1)
            down = dfs(i + 1 , j , curr + 1)
            left = dfs(i , j - 1 , curr + 1)
            right = dfs(i , j + 1 , curr + 1)
            visited.remove((i , j))
            return up or down or left or right
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i , j , 0):
                        return True
                    visited.clear()
        return False