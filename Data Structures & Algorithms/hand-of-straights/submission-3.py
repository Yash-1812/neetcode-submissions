class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        min_heap = []
        for i in count:
            heapq.heappush(min_heap , i)
        while min_heap:
            num = min_heap[0]
            if count[num] == 0:
                heapq.heappop(min_heap)
                continue
            for i in range(groupSize):
                n = num + i
                if count[n] == 0:
                    return False
                count[n] -= 1
        return True