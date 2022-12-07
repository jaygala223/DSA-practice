# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        dicti = {'ans' : 0}
        def preorder(root):
            if not root:
                return
            
            if low <= root.val <= high:
                dicti['ans'] += root.val
            
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        
        return dicti['ans']
        