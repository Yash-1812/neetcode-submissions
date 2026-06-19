class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums = sorted(nums)
        output = []
        for i in range(len(nums) - 1):
            new_target = target - nums[i] 
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > new_target:
                    right -= 1
                elif nums[left] + nums[right] < new_target:
                    left += 1
                else:
                    if [nums[i] , nums[left] , nums[right]] in output:
                        left += 1
                        right -= 1
                        continue
                    output.append([nums[i] , nums[left] , nums[right]])
                    left += 1
                    right -= 1
        return output