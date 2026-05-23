class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        def is_integer(val):
            try:
                int(val)
                return True
            except ValueError:
                return False

        stack = []
        for ch in operations:
            if is_integer(ch):
                stack.append(int(ch))
            elif ch == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num1 + num2
                stack.append(num2)
                stack.append(num1)
                stack.append(num3)
            elif ch == 'C':
                stack.pop()
            elif ch == 'D':
                num = stack[-1]
                stack.append(num * 2)

        return sum(stack)