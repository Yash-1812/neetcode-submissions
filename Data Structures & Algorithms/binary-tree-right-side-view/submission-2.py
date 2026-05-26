# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        output = []

        def level_order(r):
            queue = []
            queue.append(r)
            while queue:
                n = len(queue)
                output.append(queue[-1].val)
                for _ in range(n):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        level_order(root)
        return output
