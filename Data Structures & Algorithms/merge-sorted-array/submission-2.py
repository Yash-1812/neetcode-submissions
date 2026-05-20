class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = len(nums1) - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            
            if nums1[m] >= nums2[n]:
                nums1[m] , nums1[ptr] = nums1[ptr] , nums1[m]
                ptr -= 1
                m -= 1
            elif nums1[m] < nums2[n]:
                nums1[ptr] = nums2[n]
                n -= 1
                ptr -= 1
        
        if n >= 0:
            while n >= 0:
                nums1[ptr] = nums2[n]
                n -= 1
                ptr -= 1
        
        if m >= 0:
            while m >= 0:
                nums1[ptr] = nums1[m]
                m -= 1
                ptr -= 1

        