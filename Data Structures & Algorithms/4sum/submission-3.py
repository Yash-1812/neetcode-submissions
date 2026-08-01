class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) <= 3:
            return []
        seen = set()
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1 , len(nums) - 2):
                curr = nums[i] + nums[j]
                new_tar = target - curr
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] < new_tar:
                        left += 1
                    elif nums[left] + nums[right] > new_tar:
                        right -= 1
                    else:
                        arr = (nums[i] , nums[j] , nums[left] , nums[right])
                        if arr not in seen:
                            seen.add(arr)
                            res.append(list(arr))
                        left += 1
                        right -= 1
        return list(seen)