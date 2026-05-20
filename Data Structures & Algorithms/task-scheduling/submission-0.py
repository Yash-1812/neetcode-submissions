import heapq
from collections import Counter, deque
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        cooldown_queue = deque()
        time = 0

        while max_heap or cooldown_queue:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1

                if cnt < 0:
                    cooldown_queue.append((cnt , time + n))
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap , ready_cnt)
        
        return time
            




