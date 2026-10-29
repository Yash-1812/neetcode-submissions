class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O':
                    queue.append((i , j))
                    board[i][j] = 'E'
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr , dc in directions:
                    nr , nc = r + dr , c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if board[nr][nc] != 'O':
                        continue
                    board[nr][nc] = 'E'
                    queue.append((nr , nc))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'E':
                    board[i][j] = 'O'