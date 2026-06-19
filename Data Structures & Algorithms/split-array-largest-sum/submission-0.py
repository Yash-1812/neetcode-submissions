class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left , right = max(nums) , sum(nums)
        res = right
        def can_split(largest):
            subarrays = 0
            curr_sum = 0
            for n in nums:
                curr_sum += n
                if curr_sum > largest:
                    subarrays += 1
                    curr_sum = n
            return subarrays + 1 <= k
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res