# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findLeaf(root1) == self.findLeaf(root2)
    
    def findLeaf(self, root):
        if not root: return []
        if not root.left and not root.right: return [root.val]
        return self.findLeaf(root.left) + self.findLeaf(root.right)