class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        def addGrid(r , c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r , c) in visit or grid[r][c] == -1:
                return
            queue.append([r , c])
            visit.add((r , c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visit.add((i , j))
                    queue.append([i , j])
  
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r , c = queue.pop(0)
                grid[r][c] = dist
                addGrid(r + 1 , c)
                addGrid(r , c + 1)
                addGrid(r - 1 , c)
                addGrid(r , c - 1)
            dist += 1