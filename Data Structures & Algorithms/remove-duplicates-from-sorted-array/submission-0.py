class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(nums):
            nums[ptr1] = nums[ptr2]
            while ptr2 < len(nums) and nums[ptr1] == nums[ptr2]:
                ptr2 += 1
            ptr1 += 1
        return ptr1