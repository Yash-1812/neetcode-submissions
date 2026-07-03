# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if not list1:
            return list2
        if not list2:
            return list1
        new_head = None
        if list1.val > list2.val:
            new_head = ListNode(list2.val)
            p2 = p2.next
        else:
            new_head = ListNode(list1.val)
            p1 = p1.next
        temp = new_head
        while p1 or p2:
            if not p1:
                temp.next = p2
                break
            elif not p2:
                temp.next = p1
                break
            elif p1.val < p2.val:
                temp.next = p1
                p1 = p1.next
            else:
                temp.next = p2
                p2 = p2.next
            temp = temp.next
        return new_head