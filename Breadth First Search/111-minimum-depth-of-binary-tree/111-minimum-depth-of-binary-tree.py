# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while len(queue) > 0:
            depth += 1
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return depth
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
        return depth
        