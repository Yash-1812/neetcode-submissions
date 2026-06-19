class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        is_present = False
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        visit = set()
        def dfs(i , j , idx):
            if idx == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[idx] or (i,j) in visit:
                return False
            visit.add((i , j))
            found =  dfs(i+1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j-1,idx+1)
            visit.remove((i , j))
            return found
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    is_present = dfs(i , j , 0)
                    if is_present:
                        return is_present
        return is_present