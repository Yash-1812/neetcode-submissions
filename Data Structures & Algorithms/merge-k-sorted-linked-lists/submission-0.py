# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merge_lists = []
            for i in range(0 , len(lists) , 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merge_lists.append(self.merge(l1 , l2))
            lists = merge_lists
        return lists[0]
    def merge(self , l1 , l2):
        temp1 = l1
        temp2 = l2
        if temp1 == None:
            return temp2
        if temp2 == None:
            return temp1
        head = None
        if temp1.val < temp2.val:
            head = temp1
            temp1 = temp1.next
        else:
            head = temp2
            temp2 = temp2.next
        temp = head
        while temp1 or temp2:
            if temp1 == None:
                temp.next = temp2
                break
            elif temp2 == None:
                temp.next = temp1
                break
            elif temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        return head