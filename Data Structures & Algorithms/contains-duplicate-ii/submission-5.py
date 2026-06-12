class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        graph = collections.defaultdict(list)
        for i in range(len(nums)):
            graph[nums[i]].append(i)
        for num in nums:
            if len(graph[num]) > 1:
                if abs(graph[num][0] - graph[num][len(graph[num]) - 1]) <= k or abs(graph[num][len(graph[num]) - 1] - graph[num][len(graph[num]) - 2]) <= k:
                    return True
        return False