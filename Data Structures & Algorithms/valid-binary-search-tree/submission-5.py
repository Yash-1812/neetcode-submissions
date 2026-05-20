# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self , root , output):
        if not root:
            return 
        self.inOrder(root.left , output)
        output.append(root.val)
        self.inOrder(root.right , output)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        self.inOrder(root , output)
        for i in range(1 , len(output)):
            if output[i] <= output[i-1]:
                return False
        return True