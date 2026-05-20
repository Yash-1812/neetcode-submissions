class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if l == r and target != nums[mid]:
                if target < nums[mid]:
                    return mid
                else:
                    return mid + 1
            elif target > nums[mid]:
                l += 1
            elif target < nums[mid]:
                r -= 1
            elif target == nums[mid]:
                return mid