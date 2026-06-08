class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1) - 1 , -1 , -1):
            if nums1[i] == 0:
                nums1[i] = float('inf')
            else:
                break
        ptr1 , ptr2 = 0 , 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == float('inf'):
                nums1[ptr1] = nums2[ptr2]
                ptr1 += 1
                ptr2 += 1
                m += 1
            elif nums1[ptr1] > nums2[ptr2]:
                j = m - 1
                while j >= ptr1:
                    nums1[j + 1] = nums1[j]
                    j -= 1
                nums1[j + 1] = nums2[ptr2]
                m += 1
                ptr2 += 1
                ptr1 += 1
            else:
                ptr1 += 1