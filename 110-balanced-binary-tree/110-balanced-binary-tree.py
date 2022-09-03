# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree_height(self, root):
        if root is None:
            return 0
        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)
        
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.tree_height(root) != -1
        