# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = []
        
        def preorder(node):
            if node:
                pre.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        print(pre)
        temp = root
        
        for i in range(len(pre)):
            temp.val = pre[i]
            if i != len(pre)-1:
                nn = TreeNode()
                temp.right = nn
                temp.left = None
                temp = temp.right
        
        return root
            