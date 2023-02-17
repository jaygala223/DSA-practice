# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 1e9
        self.prev = -1e9
        
        def inorder(root):
            if not root: return
            
            inorder(root.left)
            
            self.ans = min(self.ans, abs(root.val - self.prev))
            self.prev = root.val
            
            inorder(root.right)
                
        inorder(root)
        return self.ans