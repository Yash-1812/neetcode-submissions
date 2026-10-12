class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        min_heap = [(0,0,0)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        while min_heap:
            cost , r , c = heapq.heappop(min_heap)
            if (r , c) in visited:
                continue
            visited.add((r , c))
            if (r , c) == (m - 1 , n - 1):
                return cost
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                new_cost = max(abs(heights[nr][nc] - heights[r][c]) , cost)
                heapq.heappush(min_heap , (new_cost , nr , nc))