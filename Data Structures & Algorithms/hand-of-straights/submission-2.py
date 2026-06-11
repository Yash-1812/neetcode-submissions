class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            smallest = min_heap[0]
            if count[smallest] == 0:
                heapq.heappop(min_heap)
                continue
            for i in range(groupSize):
                curr = smallest + i
                if count[curr] <= 0:
                    return False
                count[curr] -= 1
        return True