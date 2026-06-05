# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Traverse(self , root , output):
        if not root:
            return
        self.Traverse(root.left , output)
        self.Traverse(root.right , output)
        output.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.Traverse(root , output)
        return output