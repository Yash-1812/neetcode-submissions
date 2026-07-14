class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap , (-a , 'a'))
        if b > 0:
            heapq.heappush(max_heap , (-b , 'b'))
        if c > 0:
            heapq.heappush(max_heap , (-c , 'c'))
        res = []
        while max_heap:
            count , ch = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not max_heap:
                    return ''.join(res)
                count2 , ch2 = heapq.heappop(max_heap)
                res.append(ch2)
                count2 += 1
                if count2 < 0:
                    heapq.heappush(max_heap , (count2 , ch2))
                heapq.heappush(max_heap , (count , ch))
            else:
                res.append(ch)
                count += 1
                if count < 0:
                    heapq.heappush(max_heap , (count , ch))
        return ''.join(res)