# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self , root , array):
        if root == None:
            return

        self.inorder(root.left , array)
        array.append(root.val)
        self.inorder(root.right , array)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        array = []
        self.inorder(root , array)
        return array[k - 1]