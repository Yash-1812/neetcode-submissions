class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(op , close):
            if len(stack) == 2*n:
                res.append("".join(stack))
                return
            if op < n:
                stack.append('(')
                op += 1
                backtrack(op , close)
                stack.pop()
                op -= 1
            if close < op:
                stack.append(')')
                close += 1
                backtrack(op , close)
                stack.pop()
                close -= 1
        backtrack(0 , 0)
        return res