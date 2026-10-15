class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        stack = []
        for idx , height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i , hei = stack.pop()
                max_area = max(max_area , (idx - i) * hei)
                start = i
            stack.append((start , height))
        for i , hei in stack:
            max_area = max(max_area , (n - i) * hei)
        return max_area