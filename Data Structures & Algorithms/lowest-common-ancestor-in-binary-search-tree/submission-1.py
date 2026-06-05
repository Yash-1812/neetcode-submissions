# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def LCA(self , root , p , q):
        if p.val > root.val and q.val > root.val:
            return self.LCA(root.right , p , q)
        if p.val < root.val and q.val < root.val:
            return self.LCA(root.left , p , q)
        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
            return root
        if p.val == root.val or q.val == root.val:
            return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.LCA(root , p , q)