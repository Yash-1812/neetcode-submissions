class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        if target > nums[n]:
            return n + 1
        if target < nums[0]:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target < nums[mid + 1]:
                return mid + 1
            elif target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            elif target == nums[mid]:
                return mid
            