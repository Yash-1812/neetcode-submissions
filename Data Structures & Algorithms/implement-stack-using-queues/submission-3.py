class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue1) - 1):
            num = self.queue1.pop(0)
            self.queue2.append(num)
        n = self.queue1.pop(0)
        for _ in range(len(self.queue2)):
            num = self.queue2.pop(0)
            self.queue1.append(num)
        return n

    def top(self) -> int:
        return self.queue1[-1]
        

    def empty(self) -> bool:
        return True if len(self.queue1) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()