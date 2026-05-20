class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = []
        right_prod = []
        result = []
        left_prod.append(1)
        right_prod.append(1)
        for i in range(1 , len(nums)):
            curr = nums[i - 1] * left_prod[-1]
            left_prod.append(curr)
        for i in range(len(nums) - 2 , -1 , -1):
            curr = nums[i + 1] * right_prod[-1]
            right_prod.append(curr)
        right_prod.reverse()
        for i in range(len(nums)):
            result.append(left_prod[i] * right_prod[i])
        return result