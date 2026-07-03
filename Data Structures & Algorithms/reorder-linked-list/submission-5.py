# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
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
        start1 , start2 = head , prev
        while start1 and start2:
            temp1 , temp2 = start1.next , start2.next
            start1.next = start2
            start2.next = temp1
            start2 = temp2
            start1 = temp1
        