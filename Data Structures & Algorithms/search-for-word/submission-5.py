class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        def dfs(i , j , idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols or (i , j) in visited:
                return False
            if board[i][j] != word[idx]:
                return False
            visited.add((i , j))
            up = dfs(i - 1 , j , idx + 1)
            down = dfs(i + 1 , j , idx + 1)
            left = dfs(i , j - 1 , idx + 1)
            right = dfs(i , j + 1 , idx + 1)
            visited.remove((i , j))
            return up or down or left or right

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i , j , 0):
                        return True
                    visited.clear()
        return False