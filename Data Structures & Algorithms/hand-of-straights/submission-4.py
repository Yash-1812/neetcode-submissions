class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        min_heap = []
        for k in count:
            heapq.heappush(min_heap , k)
        while min_heap:
            smallest = min_heap[0]
            if count[smallest] == 0:
                heapq.heappop(min_heap)
                continue
            for i in range(groupSize):
                num = smallest + i
                if count[num] <= 0:
                    return False
                count[num] -= 1
        return True