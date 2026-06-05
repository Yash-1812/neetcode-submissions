# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def Traverse(self , root , output):
        if not root:
            return
        self.Traverse(root.left , output)
        output.append(root.val)
        self.Traverse(root.right , output)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        self.Traverse(root , output)
        for i in range(1 , len(output)):
            if output[i] <= output[i - 1]:
                return False

        return True