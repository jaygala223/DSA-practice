# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        queue = [root]
        
        zig = 1
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            level = level[:] if zig%2 else level[::-1]
            
            ans.append(level)
            zig += 1
        
        return ans
                
                
        
        