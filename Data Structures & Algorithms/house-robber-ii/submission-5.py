class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        def HouseRobber(arr):
            if len(arr) == 1:
                return arr[0]
            y = len(arr)
            arr[y - 2] = max(arr[y - 1] , arr[y - 2])
            for i in range(y - 3 , -1 , -1):
                arr[i] = max(arr[i + 1] , arr[i] + arr[i + 2])
            return arr[0]

        ar1 = HouseRobber(nums[:-1])
        ar2 = HouseRobber(nums[1:])

        return max(ar1 , ar2)