# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root, p, q):
        
            if root == p or root == q or root == None:
                return root
            
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            
            if left and right: return root
            
            return left if left else right
        
        return helper(root, p, q)
            