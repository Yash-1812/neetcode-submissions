class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i , val in enumerate(nums):
            t2 = target - val
            for j in range(i + 1 , len(nums)):
                if nums[j] == t2:
                    return [i , j]

                    