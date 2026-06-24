class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_array(left , right):
            while left < right:
                nums[left] , nums[right] = nums[right] , nums[left]
                right -= 1
                left += 1
        
        k = k % len(nums)
        reverse_array(0 , len(nums) - 1)
        reverse_array(0 , k - 1)
        reverse_array(k , len(nums) - 1)