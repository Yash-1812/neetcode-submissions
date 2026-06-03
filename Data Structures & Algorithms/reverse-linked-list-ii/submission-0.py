class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # 1. Create a dummy node to seamlessly handle left = 1
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        # 2. Move 'pre' to the node right BEFORE the sub-list starts
        for _ in range(left - 1):
            pre = pre.next
            
        # 3. 'start' is the first node of the sub-list to be reversed
        # 'then' is the node that will be moved to the front
        start = pre.next
        then = start.next
        
        # 4. Reverse the sub-list in place
        # We need to perform exactly (right - left) operations
        for _ in range(right - left):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
            
        return dummy.next