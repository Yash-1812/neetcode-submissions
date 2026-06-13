class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []
        for component in components:
            if component == '..':
                if stack:
                    stack.pop()
            elif component == '.' or component == '':
                continue
            else:
                stack.append(component)
        return '/'+'/'.join(stack)