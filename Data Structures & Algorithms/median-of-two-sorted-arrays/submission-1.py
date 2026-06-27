class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = []
        ptr1 , ptr2 = 0 , 0
        while ptr1 < len(nums1) or ptr2 < len(nums2):
            if ptr1 == len(nums1):
                for j in range(ptr2 , len(nums2)):
                    nums.append(nums2[j])
                break

            elif ptr2 == len(nums2):
                for j in range(ptr1 , len(nums1)):
                    nums.append(nums1[j])
                break

            elif nums1[ptr1] < nums2[ptr2]:
                nums.append(nums1[ptr1])
                ptr1 += 1

            else:
                nums.append(nums2[ptr2])
                ptr2 += 1
        if len(nums) % 2 != 0:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
