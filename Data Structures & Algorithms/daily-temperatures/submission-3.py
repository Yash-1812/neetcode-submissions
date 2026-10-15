class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = []
        for i in range(n - 1 , -1 , -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1][0] - i)
            stack.append((i , temperatures[i]))
        res.reverse()
        return res