class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        min_heap = [[0,0,0]]
        visit = set()
        directions = [[1,0] , [0,1] , [-1,0] , [0,-1]]
        while min_heap:
            diff , r , c = heapq.heappop(min_heap)
            if (r , c) == (m - 1 , n - 1):
                return diff
            if (r , c) in visit:
                continue
            visit.add((r , c))
            for i , j in directions:
                nr , nc = i + r , j + c
                if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr,nc) in visit:
                    continue
                d = max(diff , abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(min_heap , [d , nr , nc])