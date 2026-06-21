class ListNode:
    def __init__(self , val):
        self.next = None
        self.prev = None
        self.data = val

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.count = 0
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.limit:
            return False
        node = ListNode(value)
        if not self.head:
            self.head = node
            self.tail = node
            self.count += 1
            return True
        temp = self.tail
        temp.next = node
        node.prev = temp
        self.tail = node
        t = self.head
        node.next = t
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if not self.head:
            return False
        if self.count == 1:
            self.head , self.tail = None , None
            self.count -= 1
            return True
        temp = self.head
        self.head = temp.next
        new_head = self.head
        #temp.next , new_head.prev = None , None
        self.tail.next = new_head
        self.count -= 1
        return True

    def Front(self) -> int:
        if not self.head:
            return -1
        return self.head.data

    def Rear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.data

    def isEmpty(self) -> bool:
        if not self.head:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.limit:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()