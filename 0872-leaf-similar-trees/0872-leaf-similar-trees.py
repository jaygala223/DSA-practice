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
        sequences = {'seq1': [], 'seq2': []}
        
        def getSequence(root, seqNumber):
            if not root:
                return
            
            if root.right == None and root.left == None:
                sequences['seq' + str(seqNumber)].append(root.val)
                
            getSequence(root.left, seqNumber)
            getSequence(root.right, seqNumber)
            
        getSequence(root1, 1)
        getSequence(root2, 2)
        
        return sequences['seq1'] == sequences['seq2']