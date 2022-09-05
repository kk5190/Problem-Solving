"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        output = []
        self.dfs(root, 0, output)
        return output
    
    def dfs(self, root, level, output):
        if root is None:
            return
        if len(output) < level + 1:
            output.append([])
        output[level].append(root.val)
        for child in root.children:
            self.dfs(child, level+1, output)
        