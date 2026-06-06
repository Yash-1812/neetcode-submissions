class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def HouseRobber(arr):
            if len(arr) == 1:
                return arr[0]
            if len(arr) == 2:
                return max(arr[0] , arr[1])
            n = len(arr)
            arr[n - 2] = max(arr[n - 2] , arr[n - 1])
            for i in range(n - 3 , -1 , -1):
                arr[i] = max(arr[i] + arr[i + 2] , arr[i + 1])
            return max(arr[0] , arr[1])

        senario1 = HouseRobber(nums[:-1])
        senario2 = HouseRobber(nums[1:])

        return max(senario1 , senario2)