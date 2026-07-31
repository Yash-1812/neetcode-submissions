# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        dummy = ListNode(-1001 , None)
        res = dummy
        for i in range(len(lists)):
            l = lists[i]
            res = self.merge(res , l)
        return res.next
    def merge(self , l1 , l2):
        if not l2:
            return l1
        head = l1
        l1 = l1.next
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if not l1:
            curr.next = l2
        if not l2:
            curr.next = l1
        return head