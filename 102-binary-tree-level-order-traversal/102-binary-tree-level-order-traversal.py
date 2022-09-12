# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = [root]
        
        
        while len(queue) > 0:
            n = len(queue)
            level = []
            for _ in range(n):
                e = queue.pop(0)
                level.append(e.val)
                for child in [e.left, e.right]:
                    if child is not None:
                        queue.append(child)
            res.append(level)
        return res
            
        