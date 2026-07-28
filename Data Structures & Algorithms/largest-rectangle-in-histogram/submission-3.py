class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i , height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx , hei = stack.pop()
                max_area = max(max_area , (i - idx) * hei)
                start = idx
            stack.append((start , height))
        n = len(heights)
        for idx , hei in stack:
            max_area = max(max_area , (n - idx) * hei)
        return max_area