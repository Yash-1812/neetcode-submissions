# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        level = 0
        while queue:
            sub_arr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
            if level % 2 == 1:
                for i in range(len(queue)):
                    sub_arr.append(queue[i].val)
                n = len(sub_arr) - 1
                for i in range(len(queue)):
                    queue[i].val = sub_arr[n - i]
        return root