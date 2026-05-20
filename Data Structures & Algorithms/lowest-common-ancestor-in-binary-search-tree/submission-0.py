# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root == None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left_LCA = self.lowestCommonAncestor(root.left , p , q)
        right_LCA = self.lowestCommonAncestor(root.right , p , q)
        if left_LCA and right_LCA:
            return root
        elif left_LCA:
            return left_LCA
        else:
            return right_LCA
        