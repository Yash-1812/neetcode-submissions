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
        output.append(root.val)
        self.Traverse(root.left , output)
        self.Traverse(root.right , output)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.Traverse(root , output)
        return output