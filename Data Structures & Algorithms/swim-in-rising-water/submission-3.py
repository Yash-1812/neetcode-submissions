class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minH = [[grid[0][0] , 0 , 0]]
        visit = set()
        directions = [[1,0] , [0,1] , [-1,0] , [0,-1]]
        while minH:
            t , r , c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return  t
            for i , j in directions:
                nr , nc = r + i , c + j
                if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr , nc) in visit:
                    continue
                visit.add((nr , nc))
                heapq.heappush(minH , [max(t , grid[nr][nc]) , nr , nc])
