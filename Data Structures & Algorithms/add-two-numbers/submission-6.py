# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val1 = l1.val
                val2 = l2.val
            if not l1:
                val1 = 0
                val2 = l2.val
            if not l2:
                val1 = l1.val
                val2 = 0
            num = (val1 + val2 + carry) % 10
            node = ListNode(num)
            temp.next = node
            temp = temp.next
            carry = (val1 + val2 + carry) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            temp.next = ListNode(carry)
        return dummy.next