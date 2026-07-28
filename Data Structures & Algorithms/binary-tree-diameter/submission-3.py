# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        def diameter(root):
            if not root:
                return 0
            left_height = diameter(root.left)
            right_height = diameter(root.right)
            self.max_dia = max(self.max_dia , left_height + right_height)
            return 1 + max(left_height , right_height)
        hei = diameter(root)
        return self.max_dia