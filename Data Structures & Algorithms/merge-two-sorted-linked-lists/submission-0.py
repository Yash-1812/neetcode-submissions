# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head = ListNode(0)
        temp1 = list1
        temp2 = list2
        if temp1.val < temp2.val:
            head.val = temp1.val
            temp1 = temp1.next
        else:
            head.val = temp2.val
            temp2 = temp2.next
        curr = head
        while temp1 or temp2:
            if not temp1:
                curr.next = temp2
                break
            if not temp2:
                curr.next = temp1
                break

            if temp1.val < temp2.val:
                node = ListNode(temp1.val)
                temp1 = temp1.next
                curr.next = node
                curr = curr.next
            else:
                node = ListNode(temp2.val)
                temp2 = temp2.next
                curr.next = node
                curr = curr.next

        return head
