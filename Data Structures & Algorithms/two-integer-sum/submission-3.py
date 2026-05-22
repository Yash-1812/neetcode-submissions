class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        def required(arr , num , idx):
            for i in range(len(arr)):
                if arr[i] == num:
                    output.append(idx)
                    output.append(idx + i + 1)

        for i in range(len(nums)):
            num = target - nums[i]
            required(nums[i + 1 : len(nums) + 1] , num , i)
        
        return output
