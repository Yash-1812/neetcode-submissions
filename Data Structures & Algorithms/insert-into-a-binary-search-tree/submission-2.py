# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertion(self , root , val):
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insertion(root.right , val)
        
        elif val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insertion(root.left , val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            node = TreeNode(val)
            return node
        self.insertion(root , val)
        return root


