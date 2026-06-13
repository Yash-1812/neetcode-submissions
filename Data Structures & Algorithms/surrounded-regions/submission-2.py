class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows , cols = len(board) , len(board[0])
        visit = set()
        def isSurrounded(r , c):
            if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                return False
            queue = [(r , c)]
            visit.add((r , c))
            directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
            while queue:
                for _ in range(len(queue)):
                    dr , dc = queue.pop(0)
                    for i , j in directions:
                        nr , nc = dr + i , dc + j
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            continue
                        if nr == 0 or nc == 0 or nr == rows - 1 or nc == cols - 1:
                            if board[nr][nc] == 'O':
                                visit.clear()
                                return False
                            else:
                                continue
                        if board[nr][nc] == 'X' or (nr , nc) in visit:
                            continue
                        queue.append((nr , nc)) 
                        visit.add((nr , nc))
            return True

        def replace(i , j):
            for i , j in visit:
                board[i][j] = 'X'
            visit.clear()
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and isSurrounded(i , j):
                    replace(i , j)