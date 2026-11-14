# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(root):
            if not root:
                return 0
            left_balance = dfs(root.left)
            right_balance = dfs(root.right)
            self.moves += abs(left_balance) + abs(right_balance)
            return root.val + left_balance + right_balance - 1
        num = dfs(root)
        return self.moves