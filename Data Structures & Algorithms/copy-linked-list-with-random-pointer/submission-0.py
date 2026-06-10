"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        address = {}
        curr = head
        while curr:
            address[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new_node = address[curr]
            new_node.next = address.get(curr.next)
            new_node.random = address.get(curr.random)
            curr = curr.next
        return address[head]
