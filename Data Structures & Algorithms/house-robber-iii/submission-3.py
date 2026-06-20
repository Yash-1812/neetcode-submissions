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
                return [0,0]  #[with_root , without_root]
            
            left = dfs(root.left)   #[0,0]
            right = dfs(root.right)  #[0,0]

            with_root = root.val + left[1] + right[1]
            without_root = max(left) + max(right)

            return [with_root , without_root]
        
        return max(dfs(root))