class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = [(r, c)]
            visited.add((r, c))
            
            while queue:
                r_, c_ = queue.pop(0)
                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                
                for dr, dc in directions:
                    nr, nc = r_ + dr, c_ + dc
                    
                
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == '1' and 
                        (nr, nc) not in visited):
                        
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands