class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ptr1 = 0
        ptr2 = k
        output = []

        def find_max(arr):
            max_ele = -float('inf')
            for i in arr:
                if i > max_ele:
                    max_ele = i
            return max_ele

        while ptr2 <= len(nums):
            max_ele = find_max(nums[ptr1:ptr2])
            output.append(max_ele)
            ptr1 += 1
            ptr2 += 1

        return output
