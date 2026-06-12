class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        visit = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    queue.append((i,j))
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        while queue:
            for _ in range(len(queue)):
                dr , dc = queue.pop(0)
                for i , j in directions:
                    nr , nc = dr + i , dc + j
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == -1 or (nr,nc) in visit:
                        continue
                    grid[nr][nc] = grid[dr][dc] + 1
                    visit.add((nr,nc))
                    queue.append((nr,nc))

