class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()
        for i in range(len(nums)):
            target = -nums[i]
            left , right = i + 1 , len(nums) - 1
            while left < right:
                if ((nums[left] + nums[right]) == target) and (nums[i] , nums[left] , nums[right]) not in visited:
                    res.append([nums[i] , nums[left] , nums[right]].copy())
                    visited.add((nums[i] , nums[left] , nums[right]))
                    left += 1
                    right -= 1
                elif ((nums[left] + nums[right]) < target):
                    left += 1
                else:
                    right -= 1
        return res