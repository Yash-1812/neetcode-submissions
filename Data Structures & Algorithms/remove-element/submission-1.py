class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
        
        ptr = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != -1:
                nums[ptr] = nums[i]
                ptr += 1
                k += 1

        return k