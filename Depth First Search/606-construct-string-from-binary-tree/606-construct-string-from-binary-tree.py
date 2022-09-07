# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ''
            left = dfs(node.left)
            right = dfs(node.right)
            

            s = f'{node.val}'
            if left:
                s += f'({left})'
                
            if right:
                if not left:
                    s += '()'
                s += f'({right})'
            return s
        return dfs(root)
        