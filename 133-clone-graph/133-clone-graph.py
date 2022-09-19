"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeMap = {} #mapping old nodes to new
        
        def clone(node):
            if node in nodeMap:
                return nodeMap[node] #return the new node
            
            copy = Node(node.val)
            nodeMap[node] = copy #copy created and added to map
            
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        return clone(node) if node else None
                