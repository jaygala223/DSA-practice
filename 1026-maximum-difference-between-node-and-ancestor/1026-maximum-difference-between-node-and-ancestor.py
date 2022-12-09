# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.helper(root, maxi = -1e9, mini = 1e9)
    
    def helper(self, root, maxi, mini):
        if not root:
            return maxi - mini
        
        maxi = max(maxi, root.val)
        mini = min(mini, root.val)
        
        return max(self.helper(root.left, maxi, mini), self.helper(root.right, maxi, mini))
        
        
        
        