# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        k = length - n
        idx = 1
        if k == 0:
            return head.next if head.next else None
        prev = head
        curr = head.next
        while curr:
            if idx == k:
                prev.next = curr.next
                curr.next = None
                return head
            idx += 1
            prev = curr
            curr = curr.next