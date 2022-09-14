# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        q = [root]
        while len(q) > 0:
            n = len(q)
            res.append(q[0].val)
            for _ in range(n):
                node = q.pop(0)
                for child in [node.right, node.left]:
                    if child is not None:
                        q.append(child)
        return res
        