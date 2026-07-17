class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        min_heap = [(0 , 0 , 0)]
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        visited = set()
        while min_heap:
            diff , r , c = heapq.heappop(min_heap)
            if (r , c) == (rows - 1 , cols - 1):
                return diff
            if (r , c) in visited:
                continue
            visited.add((r , c))
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr , nc) in visited:
                    continue
                new_diff = max(diff , abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(min_heap , (new_diff , nr , nc))