# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        k = length - n
        if k == 0:
            temp = head
            head = temp.next
            return head
        c = 0
        curr = head
        prev = None
        while c < k:
            prev = curr
            curr = curr.next
            c += 1
        prev.next = curr.next
        curr.next = None
        return head