class Solution:
    def reorganizeString(self, s: str) -> str:
        count_chars = Counter(s)
        max_heap = []
        for c in count_chars:
            heapq.heappush(max_heap , (-count_chars[c] , c))
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ''
        prev_char , prev_count = '' , 0
        res = []
        while max_heap:
            count , ch = heapq.heappop(max_heap)
            res.append(ch)
            if prev_count < 0:
                heapq.heappush(max_heap , (prev_count , prev_char))
            count += 1
            prev_char , prev_count = ch , count
        return ''.join(res)