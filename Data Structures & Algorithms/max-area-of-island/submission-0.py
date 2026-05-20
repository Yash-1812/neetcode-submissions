class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        def bfs(r , c):
            queue = [(r,c)]
            visited.append((r,c))
            directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
            count_Area = 1
            while queue:
                r_ , c_ = queue.pop(0)
                for dr , dc in directions:
                    nr , nc = r_ + dr , c_ + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1 and
                        (nr , nc) not in visited):
                        queue.append((nr,nc))
                        visited.append((nr,nc))
                        count_Area += 1
            return count_Area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r , c)
                    max_area = max(max_area , area)
        
        return max_area
        