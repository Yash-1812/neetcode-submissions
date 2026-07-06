class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_list = {i : [] for i in range(N)}
        for i in range(N):
            x1 , y1 = points[i]
            for j in range(i + 1 , N):
                x2 , y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append([j , dist])
                adj_list[j].append([i , dist])
        min_heap = [(0 , 0)]   # (dist , node)
        visited = set()
        res = 0
        while len(visited) < N: 
            dist , node = heapq.heappop(min_heap)
            if node in visited:
                continue
            res += dist
            visited.add(node)
            for nei , cost in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(min_heap , (cost , nei))
        return res