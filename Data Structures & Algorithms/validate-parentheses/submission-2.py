class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if ch == ')' and stack[-1] != '(':
                    return False
                if ch == '}' and stack[-1] != '{':
                    return False
                if ch == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        return True if len(stack) == 0 else False