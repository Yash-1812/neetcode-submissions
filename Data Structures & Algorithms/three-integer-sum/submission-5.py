class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()
        for i in range(len(nums)):
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    if tuple([nums[i] , nums[left] , nums[right]]) not in visited:
                        visited.add(tuple([nums[i] , nums[left] , nums[right]]))
                        res.append([nums[i] , nums[left] , nums[right]])
                    left += 1
                    right -= 1
        return res