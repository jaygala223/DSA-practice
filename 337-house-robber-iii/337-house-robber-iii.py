# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def func(root):
            ##tuple-> (withroot, withoutroot)
            
            if not root: return (0,0)
            
            left, right = func(root.left), func(root.right)
            
            #next level ke root ko nahi lena
            withroot = root.val + left[1] + right[1]
            
            #next level le sakte h
            withoutroot = max(left) + max(right)
                
            return (withroot, withoutroot)
        
        return max(func(root))