class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_list = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complement_list:
                return [complement_list[complement] , i]
            complement_list[nums[i]] = i
