class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ptr1 = 0
        ptr2 = k
        res = []
        while ptr2 <= len(nums):
            val = max(nums[ptr1:ptr2])
            res.append(val)
            ptr1 += 1
            ptr2 += 1
        return res