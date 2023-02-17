# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.ans, self.parent = 1e9, -1e9
        
        def inorder(root):
            if self.ans != 1:
                if not root: return

                inorder(root.left)

                self.ans = min(self.ans, abs(root.val - self.parent))
                self.parent = root.val

                inorder(root.right)
        
        inorder(root)
        return self.ans