# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def Check(self , node , sub_node):
        if node == None and sub_node == None:
            return True
        if node == None or sub_node == None:
            return False
        if node.val != sub_node.val:
            return False
        return self.Check(node.left , sub_node.left) and self.Check(node.right , sub_node.right) 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if root.val == subRoot.val and self.Check(root , subRoot):
            return True
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)
        
        