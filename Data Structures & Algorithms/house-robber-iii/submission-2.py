# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return [0,0]   #[with_root , without_root]
            
            left_root = dfs(root.left)
            right_root = dfs(root.right)

            with_root = root.val + left_root[1] + right_root[1]
            without_root = max(left_root) + max(right_root)

            return [with_root , without_root]
        
        return (max(dfs(root)))