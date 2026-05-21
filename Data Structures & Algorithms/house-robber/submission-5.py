class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        robber = []
        robber.append(nums[0])
        robber.append(max(nums[1] , nums[0]))

        for i in range(2 , len(nums)):
            robber.append(max(nums[i] + robber[i - 2] , robber[i - 1]))

        return max(robber)

