# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        t = head
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        temp1 , temp2 = list1 , list2
        while temp1 or temp2:
            if temp1 == None:
                t.next = temp2
                break
            elif temp2 == None:
                t.next = temp1
                break
            elif temp1.val < temp2.val:
                t.next = temp1
                t = t.next
                temp1 = temp1.next
            elif temp1.val >= temp2.val:
                t.next = temp2
                t = t.next
                temp2 = temp2.next
        
        return head.next
