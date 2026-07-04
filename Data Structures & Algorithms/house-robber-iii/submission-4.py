# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = -float('inf')
        def dfs(root):
            if not root:
                return [0, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            with_root = root.val + left[1] + right[1]
            without_root = max(left) + max(right)
            self.max_path_sum = max(self.max_path_sum, with_root, without_root)
            return [with_root, without_root]
        dfs(root)
        return self.max_path_sum