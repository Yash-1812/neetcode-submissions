class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0 , len(heights) - 1
        max_vol = 0
        while left < right:
            max_vol = max(max_vol , min(heights[left] , heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_vol