class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        count = collections.defaultdict(int)
        for num in nums:
            if num in count:
                c = count[num]
            else:
                c = 0
            count[num] += 1
            heapq.heappush(max_heap , (-(c + 1) , num))
        output = []
        visit = set()
        i = 0
        while i < k:
            c , num = heapq.heappop(max_heap)
            if num in visit:
                continue
            visit.add(num)
            output.append(num)
            i += 1
        return output