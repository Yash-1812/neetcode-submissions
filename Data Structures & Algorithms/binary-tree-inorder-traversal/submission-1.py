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
        output.append(root.val)
        self.Traverse(root.right , output)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.Traverse(root , output)
        return output