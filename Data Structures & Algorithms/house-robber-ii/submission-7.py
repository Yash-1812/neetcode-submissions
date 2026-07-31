class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        def HouseRobber(arr):
            x = len(arr)
            if x == 1:
                return arr[0]
            arr[x - 2] = max(arr[x - 1] , arr[x - 2])
            for i in range(x - 3 , -1 , -1):
                arr[i] = max(arr[i + 1] , arr[i] + arr[i + 2])
            return max(arr)
        r1 = HouseRobber(nums[1:])
        r2 = HouseRobber(nums[:-1])
        return max(r1 , r2)