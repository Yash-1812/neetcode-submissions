class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                word = []
                while stack and stack[-1] != '[':
                    word.append(stack.pop())
                stack.pop()
                times = ''
                while stack and stack[-1].isdigit():
                    times += stack.pop()
                times = times[::-1]
                t = int(times)
                new_word = ''.join(reversed(word)) * t
                stack.append(new_word)
                continue
            stack.append(ch)
        return ''.join(stack)