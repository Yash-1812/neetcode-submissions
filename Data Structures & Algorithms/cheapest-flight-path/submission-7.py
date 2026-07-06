class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = collections.defaultdict(set)
        for u , v , w in flights:
            adj_list[u].add((v , w))
        min_heap = [(0 , 0 , src)]
        stops = [float('inf')] * n
        while min_heap:
            cost , stop , node = heapq.heappop(min_heap)
            if stop > k:
                continue
            if node == dst:
                return cost
            if stop >= stops[node]:
                continue
            stops[node] = stop
            for nei , c in adj_list[node]:
                if nei != dst:
                    new_stop = stop + 1
                    new_cost = c + cost
                    heapq.heappush(min_heap , (new_cost , new_stop , nei))
                else:
                    new_cost = c + cost
                    heapq.heappush(min_heap , (new_cost , stop , nei))
        return -1        