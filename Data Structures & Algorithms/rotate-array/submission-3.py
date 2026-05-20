class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse_array(nums , start , end):
            while start < end:
                nums[start] , nums[end] = nums[end] , nums[start]
                start += 1
                end -= 1

        x = len(nums) - k
        reverse_array(nums , 0 , x - 1)
        reverse_array(nums , x , len(nums) - 1)
        reverse_array(nums , 0 , len(nums) - 1)

