class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        res = []
        board = [['.'] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                copy = [''.join(rows) for rows in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                board[r][c] = '.'
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
        backtrack(0)
        return res