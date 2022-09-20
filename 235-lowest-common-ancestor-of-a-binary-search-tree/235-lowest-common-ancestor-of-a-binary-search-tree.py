# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pv, qv = p.val, q.val
        
        while root:
            rv = root.val
            
            #ek left me ek right mein
            if qv > rv > pv or pv > rv > qv:
                return root
            
            #jo pehle mil gaya wohi root
            if root == p or root == q:
                return root
            
            if pv > rv: root = root.right
            else: root = root.left
        return None