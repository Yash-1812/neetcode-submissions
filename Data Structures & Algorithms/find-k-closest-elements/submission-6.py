class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []   # (diff , idx)
        for i , num in enumerate(arr):
            diff = abs(num - x)
            heapq.heappush(min_heap , (diff , i))
        output = []
        for _ in range(k):
            diff , idx = heapq.heappop(min_heap)
            output.append(arr[idx])
        output.sort()
        return output