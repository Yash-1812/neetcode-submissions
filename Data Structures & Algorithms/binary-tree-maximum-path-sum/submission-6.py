# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float('inf')
        def Path(root):
            if not root:
                return 0
            left_sum = max(0 , Path(root.left))
            right_sum = max(0 , Path(root.right))
            self.max_sum = max(self.max_sum , root.val + left_sum + right_sum)
            return root.val + max(left_sum , right_sum)
        num = Path(root)
        return self.max_sum 