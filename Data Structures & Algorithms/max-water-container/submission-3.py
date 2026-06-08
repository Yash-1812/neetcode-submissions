class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0 , len(heights) - 1
        vol = 0
        while left < right:
            vol = max(vol , (min(heights[left] , heights[right]) * (right - left)))
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
        return vol