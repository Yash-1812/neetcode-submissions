from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        fresh = 0

        def rot_next(r , c):
            nonlocal fresh
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in visited:
                return
            grid[r][c] = 2
            fresh -= 1
            queue.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        time = 0
        while queue:
            for _ in range(len(queue)):
                r , c = queue.popleft()
                rot_next(r + 1 , c)
                rot_next(r , c + 1)
                rot_next(r - 1 , c)
                rot_next(r , c - 1)
            time += 1

        return time - 1 if fresh == 0 else -1


