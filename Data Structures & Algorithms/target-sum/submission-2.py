class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = collections.defaultdict(int)
        def backtrack(i , curr_sum):
            if (curr_sum , i) in memo:
                return memo[(curr_sum , i)]
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
            add = backtrack(i + 1 , curr_sum + nums[i])
            subtract = backtrack(i + 1 , curr_sum - nums[i])
            memo[(curr_sum , i)] = add + subtract
            return add + subtract
        return backtrack(0 , 0)