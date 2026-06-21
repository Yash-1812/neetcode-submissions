from collections import Counter
class FreqStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        freq = Counter(self.stack)
        max_value = max(freq.values())
        for i in range(len(self.stack) - 1 , -1 , -1):
            if freq[self.stack[i]] == max_value:
                max_key = self.stack[i]
                del self.stack[i]
                break
        return max_key

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()