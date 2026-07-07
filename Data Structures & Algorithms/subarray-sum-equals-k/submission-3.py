class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] += 1
        for num in nums:
            curr_sum += num

            if (curr_sum - k) in prefix_sum:
                count += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] += 1
        return count