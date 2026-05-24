class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        output = []

        def backtrack(openN , closeN):
            if openN == n == closeN:
                output.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1 , closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backtrack(openN , closeN + 1)
                stack.pop()

        backtrack(0 , 0)
        return output
            