# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mini, maxi = -1e11, 1e11
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(root, mini, maxi):
            if not root: return True
            
            leftTree = checkBST(root.left, mini, root.val)
            rightTree = checkBST(root.right, root.val, maxi)
            
            if root.val <= mini or root.val >= maxi: return False
            return leftTree and rightTree
        
        return checkBST(root, self.mini, self.maxi)