class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        l = len(self.queue1)
        for i in range(l - 1):
            self.queue2.append(self.queue1.pop(0))
        num = self.queue1.pop(0)
        self.queue1 = self.queue2.copy()
        self.queue2.clear()
        return num

    def top(self) -> int:
        l = len(self.queue1)
        for i in range(l - 1):
            self.queue2.append(self.queue1.pop(0))
        num = self.queue1.pop(0)
        self.queue2.append(num)
        self.queue1 = self.queue2.copy()
        self.queue2.clear()
        return num


    def empty(self) -> bool:
        return True if len(self.queue1) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()