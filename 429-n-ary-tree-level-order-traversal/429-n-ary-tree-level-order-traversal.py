"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        ans = []
        queue = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            level = []
            
            for i in range(size):
                node = queue.pop(0)
                #queue.pop()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            
            ans.append(level[:])
        
        return ans
            
            
            
            