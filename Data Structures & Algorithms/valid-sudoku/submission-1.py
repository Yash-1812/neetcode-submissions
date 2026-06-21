class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m , n = len(board) , len(board[0])
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        b = collections.defaultdict(set)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in b[(i//3 , j//3)]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                b[(i//3 , j//3)].add(board[i][j])
        return True