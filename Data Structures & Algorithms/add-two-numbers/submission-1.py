class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        
        dummy = ListNode(0)
        temp = dummy
        
        carry = 0
        
        while ptr1 or ptr2 or carry:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0
            
            total = val1 + val2 + carry
            
            carry = total // 10
            newNode = ListNode(total % 10)
            
            temp.next = newNode
            temp = temp.next
            
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        
        return dummy.next