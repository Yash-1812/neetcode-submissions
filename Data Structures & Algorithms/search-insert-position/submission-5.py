class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        n = len(nums) - 1
        if target > nums[n]:
            return n + 1
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target < nums[mid + 1]:
                return mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                return mid
                