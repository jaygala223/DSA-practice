# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = -1001
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def func(node):
            if not node: return 0
            
            lsum = max(func(node.left), 0)
            rsum = max(func(node.right),0)
            
            self.maxi = max(self.maxi, lsum + rsum + node.val)
            
            return node.val + max(lsum, rsum)
        
        func(root)
        return self.maxi