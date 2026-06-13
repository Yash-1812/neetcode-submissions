class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        temp = []
        while self.stack and self.stack[-1] <= price:
            span += 1
            temp.append(self.stack.pop())
        temp.insert(0 , price)
        while temp:
            self.stack.append(temp.pop())
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)