# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        list_length = 0
        curr = head
        while curr:
            list_length += 1
            curr = curr.next
        rev = list_length - n + 1
        if list_length == 1 and n == 1:
            head = None
            return head
        if rev == 1:
            head = head.next
            return head
        check = 1
        curr = head
        prev = None
        while curr:
            if check == rev:
                prev.next = curr.next
                curr.next = None
            prev = curr
            curr = curr.next
            check += 1
        return head


