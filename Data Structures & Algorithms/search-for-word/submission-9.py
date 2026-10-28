class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        def dfs(i , j , idx):
            if idx == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i , j) in visited:
                return False
            if board[i][j] != word[idx]:
                return False
            visited.add((i , j))
            up = dfs(i - 1 , j , idx + 1)
            down = dfs(i , j - 1 , idx + 1)
            right = dfs(i + 1 , j , idx + 1)
            left = dfs(i , j + 1 , idx + 1)
            visited.remove((i , j))
            return up or left or down or right 
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i , j , 0):
                        return True
        return False