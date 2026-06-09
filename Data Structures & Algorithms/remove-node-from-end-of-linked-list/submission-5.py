# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        x = count - n
        c = 0
        curr = head
        prev = None

        if x == 0:
            temp = head
            head = temp.next
            return head

        while curr:
            if c == x:
                prev.next = curr.next
                curr.next = None
                break
            c += 1
            prev = curr
            curr = curr.next

        return head