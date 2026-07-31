class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        min_heap = [(grid[0][0] , 0 , 0)]
        visited = set()
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        visited.add((0 , 0))
        while min_heap:
            cost , dr , dc = heapq.heappop(min_heap)
            if dr == N - 1 and dc == N - 1:
                return cost
            for r , c in directions:
                nr , nc = dr + r , dc + c
                if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr , nc) in visited:
                    continue
                visited.add((nr , nc))
                heapq.heappush(min_heap , (max(cost , grid[nr][nc]) , nr , nc)) 