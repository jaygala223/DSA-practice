# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lcaBST(root):
            if root == p or root == q or not root:
                return root
            left = lcaBST(root.left)
            right = lcaBST(root.right)
            
            if left and right: return root
            
            return left if left else right
        
        return lcaBST(root)