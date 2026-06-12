class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif ch == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif ch == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            elif ch == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2/n1))
            else:
                stack.append(int(ch))
        return stack[0]
