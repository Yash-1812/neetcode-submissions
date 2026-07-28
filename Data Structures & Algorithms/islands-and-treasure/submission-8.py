class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i , j))
                    visited.add((i , j))
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        path_length = 1
        while queue:
            for _ in range(len(queue)):
                dr , dc = queue.popleft()
                for r , c in directions:
                    nr , nc = dr + r , dc + c
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if grid[nr][nc] == -1 or (nr , nc) in visited:
                        continue
                    grid[nr][nc] = path_length
                    visited.add((nr , nc))
                    queue.append((nr , nc))
            path_length += 1
        