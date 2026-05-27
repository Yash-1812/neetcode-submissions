class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1 = 0
        ptr2 = 0
        main = []
        while ptr1 < len(nums1) or ptr2 < len(nums2):
            if ptr1 == len(nums1):
                main.append(nums2[ptr2])
                ptr2 += 1
                continue
            if ptr2 == len(nums2):
                main.append(nums1[ptr1])
                ptr1 += 1
                continue
               
            if nums1[ptr1] < nums2[ptr2]:
                main.append(nums1[ptr1])
                ptr1 += 1
                continue
            if nums1[ptr1] >= nums2[ptr2]:
                main.append(nums2[ptr2])
                ptr2 += 1
        if len(main) % 2 == 0:
            n = len(main)
            return ((main[(n//2) - 1]) + main[n // 2]) / 2
        else:
            return main[len(main) // 2]
