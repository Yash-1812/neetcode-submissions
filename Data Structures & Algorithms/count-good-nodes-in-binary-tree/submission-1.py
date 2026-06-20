# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self , root , maxval):
        if not root:
            return
        if root.val >= maxval:
            self.count += 1
        self.check(root.left , max(root.val , maxval))
        self.check(root.right , max(root.val , maxval))

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.check(root , -101)
        return self.count