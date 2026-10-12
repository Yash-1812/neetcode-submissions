class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_vol = 0
        while left < right:
            max_vol = max(max_vol , (right - left) * min(heights[left] , heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_vol