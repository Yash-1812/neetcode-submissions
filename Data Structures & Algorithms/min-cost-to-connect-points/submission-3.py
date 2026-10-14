class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_list = collections.defaultdict(set)
        for i in range(N):
            x1 , y1 = points[i]
            for j in range(i + 1 , N):
                x2 , y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].add((j , dist))
                adj_list[j].add((i , dist))
        min_heap = [(0 , 0)]
        visited = set()
        res = 0
        while len(visited) < N:
            dist , node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res += dist
            for nei , wei in adj_list[node]:
                heapq.heappush(min_heap , (wei , nei))
        return res