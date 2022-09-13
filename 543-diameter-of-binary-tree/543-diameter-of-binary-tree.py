# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diameter(root):
            if not root: return 0
            
            lh = diameter(root.left)
            rh = diameter(root.right)
            self.maxi = max(self.maxi, lh+rh)
            
            return 1 + max(lh, rh)
        
        
        diameter(root)
        return self.maxi
            