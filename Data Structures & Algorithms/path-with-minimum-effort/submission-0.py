class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        visit = set()
        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        min_heap = [[0 , 0 , 0]]       #[diff , r , c]
        while min_heap:
            diff , r , c = heapq.heappop(min_heap)
            if (r , c) in visit:
                continue
            visit.add((r , c))
            if (r , c) == (rows - 1 , cols - 1):
                return diff
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr , nc) in visit:
                    continue
                h = max(diff , abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(min_heap , (h , nr , nc))
