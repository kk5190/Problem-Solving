# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, min_val, max_val):
            if root is None:
                return True
            if not (min_val < root.val < max_val):
                return False
            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
        return dfs(root, float("-inf"), float("inf"))
        