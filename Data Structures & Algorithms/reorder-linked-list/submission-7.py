# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        s1 = head
        s2 = prev
        i = 0
        while s1 and s2:
            if i % 2 == 0:
                nxt = s1.next
                s1.next = s2
                s1 = nxt
            else:
                nxt = s2.next
                s2.next = s1
                s2 = nxt
            i += 1