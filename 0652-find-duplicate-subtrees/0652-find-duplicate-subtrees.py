# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def trv(root):
            if not root: return "null"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct
        
        nodes = collections.defaultdict(list)
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]