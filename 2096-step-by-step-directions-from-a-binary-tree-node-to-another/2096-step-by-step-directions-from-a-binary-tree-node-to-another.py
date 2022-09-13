# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ans = ""
        
        def pathfinder(root, val, path):
            
            if root.val == val: return True
            
            if root.left and pathfinder(root.left, val, path):
                path += 'L'
            
            elif root.right and pathfinder(root.right, val, path):
                path += 'R'
            
            return path
        
        s, d = [], []
        pathfinder(root, startValue, s)
        pathfinder(root, destValue, d)
        
        print(s, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))