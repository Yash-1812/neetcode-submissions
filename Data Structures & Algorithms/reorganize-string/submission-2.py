from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)
        max_heap = [[-counts , char] for char , counts in char_counts.items()]
        prev_count , prev_char = 0 , ""
        res = []
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""
        while max_heap:
            count , char = heapq.heappop(max_heap)
            res.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap , [prev_count , prev_char])
            count += 1
            prev_count , prev_char = count , char
        return "".join(res)