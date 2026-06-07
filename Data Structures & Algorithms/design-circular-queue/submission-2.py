class ListNode:
    def __init__(self, val):
        self.next = None
        self.data = val

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None  # Added to easily track the end of the queue
        self.limit = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.limit:
            return False
        
        node = ListNode(value)
        if self.count == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        # Maintain the circular connection at all times
        self.tail.next = self.head
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head  # Keep the circle closed
            
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.data

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.data  # No loop needed, simply return tail's data

    def isEmpty(self) -> bool:
        return self.count == 0
        
    def isFull(self) -> bool:
        return self.count == self.limit