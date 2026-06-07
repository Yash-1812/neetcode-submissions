# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(n1 , n2):
            res = 1
            for i in range(1 , min(n1 , n2) + 1):
                if n1 % i == 0 and n2 % i == 0:
                    res = i
            return res
        
        prev = head
        curr = head.next
        while curr:
            div = gcd(curr.val , prev.val)
            node = ListNode(div)
            prev.next = node
            node.next = curr
            prev = curr
            curr = curr.next
        return head
