# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = [root]
        left_to_right = True
        while len(queue) > 0:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            if not left_to_right:
                level.reverse()
            res.append(level)
            left_to_right = not left_to_right
        return res
        