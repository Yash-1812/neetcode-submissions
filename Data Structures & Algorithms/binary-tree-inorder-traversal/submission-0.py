# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self , root , output):
        if not root:
            return
        self.inOrder(root.left , output)
        output.append(root.val)
        self.inOrder(root.right , output)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.inOrder(root , output)
        return output