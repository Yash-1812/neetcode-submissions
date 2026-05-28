class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == '+':
                n1 = len(stack) - 1
                n2 = len(stack) - 2
                stack.append(stack[n1] + stack[n2])
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                x = stack[-1]
                stack.append(x * 2)
            else:
                stack.append(int(i))
        return sum(stack)