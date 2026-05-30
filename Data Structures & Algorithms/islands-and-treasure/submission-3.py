class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def addGrid(r , c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or (r , c) in visit:
                return
            visit.add((r , c))
            q.append([r , c])
        
        visit = set()
        q = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i , j])
                    visit.add((i , j))
        dist = 0
        while q:
            for _ in range(len(q)):
                r , c = q.pop(0)
                grid[r][c] = dist
                addGrid(r + 1 , c)
                addGrid(r , c + 1)
                addGrid(r - 1 , c)
                addGrid(r , c - 1)
            dist += 1