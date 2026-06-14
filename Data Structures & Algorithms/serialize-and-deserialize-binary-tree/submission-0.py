# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s = []
        def preorder(root):
            if not root:
                self.s.append('N')
                return
            self.s.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(self.s)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(',')
        token_item = iter(tokens)
        def helper():
            val = next(token_item)

            if val == 'N':
                return None
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()
            return root
        return helper()
        

