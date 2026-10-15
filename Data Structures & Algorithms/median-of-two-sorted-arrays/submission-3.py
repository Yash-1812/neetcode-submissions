class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        max_heap = []
        min_heap = []
        ptr1 , ptr2 = 0 , 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] <= nums2[ptr2]:
                while max_heap and max_heap[0] < nums1[ptr1]:
                    num = heapq.heappop(max_heap)
                    heapq.heappush(min_heap , -num)
                heapq.heappush(min_heap , -nums1[ptr1])
                ptr1 += 1
            else:
                while max_heap and max_heap[0] < nums2[ptr2]:
                    num = heapq.heappop(max_heap)
                    heapq.heappush(min_heap , -num)
                heapq.heappush(min_heap , -nums2[ptr2])
                ptr2 += 1
            
            while len(min_heap) > len(max_heap) + 1:
                num = -heapq.heappop(min_heap)
                heapq.heappush(max_heap , num)
        while ptr1 < len(nums1):
            while max_heap and max_heap[0] < nums1[ptr1]:
                num = heapq.heappop(max_heap)
                heapq.heappush(min_heap , -num)
            heapq.heappush(min_heap , -nums1[ptr1])
            ptr1 += 1
        while ptr2 < len(nums2):
            while max_heap and max_heap[0] < nums2[ptr2]:
                num = heapq.heappop(max_heap)
                heapq.heappush(min_heap , -num)
            heapq.heappush(min_heap , -nums2[ptr2])
            ptr2 += 1
        while len(min_heap) > len(max_heap) + 1:
            num = -heapq.heappop(min_heap)
            heapq.heappush(max_heap , num)
        if len(min_heap) == len(max_heap):
            return (-min_heap[0] + max_heap[0]) / 2
        else:
            return -min_heap[0]