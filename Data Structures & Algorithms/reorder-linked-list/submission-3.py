# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        temp , prev = second , None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        first , second = head , prev
        while first and second:
            temp1 , temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2