# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        sequences = {1: [], 2: []}
        
        def getSequence(root, seqNumber):
            if not root:
                return
            
            if not root.right and not root.left:
                sequences[seqNumber].append(root.val)
                
            getSequence(root.left, seqNumber)
            getSequence(root.right, seqNumber)
            
        getSequence(root1, 1)
        getSequence(root2, 2)
        
        return sequences[1] == sequences[2]