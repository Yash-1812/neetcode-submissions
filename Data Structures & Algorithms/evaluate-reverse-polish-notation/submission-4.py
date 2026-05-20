import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack_sum = num2 + num1
                stack.append(stack_sum)
            elif ch == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack_prod = num2 * num1
                stack.append(stack_prod)
            elif ch == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack_subtract = num2 - num1
                stack.append(stack_subtract)
            elif ch == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                if num1 > 0 and num2 > 0:
                    stack_div = num2 // num1
                else:
                    stack_div = math.ceil(num2 / num1)
                stack.append(stack_div)
            else:
                stack.append(int(ch))
        return stack[-1]