class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.stack = collections.defaultdict(int)
        self.freq = collections.defaultdict(list)

    def push(self, val: int) -> None:
        self.stack[val] += 1
        f = self.stack[val]
        if f > self.max_freq:
            self.max_freq = f
        self.freq[f].append(val)  

    def pop(self) -> int:
        val = self.freq[self.max_freq].pop()
        self.stack[val] -= 1
        if not self.freq[self.max_freq]:
            self.max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()