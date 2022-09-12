# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        def preorder(node, ans):
            if node:
                ans.append(node.val)
                preorder(node.left, ans)
                preorder(node.right, ans)
        
        preorder(root, ans)
        
        return ans