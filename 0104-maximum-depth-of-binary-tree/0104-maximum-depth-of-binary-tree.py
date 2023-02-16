# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def dfs(root, depth):
            if root:
                # print(root.val)
                dfs(root.left, depth+1)
                dfs(root.right, depth+1)
            self.ans = max(self.ans, depth)
        
        dfs(root, 0)
        
        return self.ans