class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0] , nums[1])

        nums2 = nums.copy()
        nums2.pop(0)
        nums[1] = max(nums[0] , nums[1])
        max_rob_1 = max(nums[0] , nums[1])

        for i in range(2 , len(nums) - 1):
            nums[i] = max(nums[i] + nums[i - 2] , nums[i - 1])
            max_rob_1 = max(nums[i] , nums[i - 1])
        
        
        nums2[1] = max(nums2[0] , nums2[1])
        max_rob_2 = max(nums2[0] , nums2[1])
        for i in range(2 , len(nums2)):
            nums2[i] = max(nums2[i] + nums2[i - 2] , nums2[i - 1])
            max_rob_2 = max(nums2[i] , nums2[i - 1])

        return max(max_rob_1 , max_rob_2)
 
        