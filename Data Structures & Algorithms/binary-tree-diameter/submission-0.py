# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self , root):
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        diameter = left_height + right_height
        self.max_dia = max(self.max_dia , diameter)
        return 1 + max(left_height , right_height)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        self.height(root)
        return self.max_dia