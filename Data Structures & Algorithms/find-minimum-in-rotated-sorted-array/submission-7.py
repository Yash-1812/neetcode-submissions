class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums) - 1
        min_num = nums[left]
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
