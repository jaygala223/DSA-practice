# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxPath = -1001
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def solve(root):
            if not root: return 0
            
            leftSum = max(solve(root.left), 0)
            rightSum = max(solve(root.right), 0)
            
            currSum = leftSum + rightSum + root.val
            self.maxPath = max(self.maxPath, currSum)
            
            return max(leftSum, rightSum) + root.val
        
        solve(root)
        return self.maxPath