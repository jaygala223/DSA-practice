# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        ds = defaultdict(list)
        
        def func(root, row, col, ds):
            if not root: return
            
            left = func(root.left, row+1, col-1, ds)
            right = func(root.right, row+1, col+1, ds)
            
            #tuple(row, value)
            ds[col].append((row, root.val))
        
        func(root, 0, 0, ds)
        
        for key in sorted(list(ds.keys())):
            nodes = ds[key]
            nodes.sort()
            vertical = []
            for i in nodes:
                vertical.append(i[1])
            ans.append(vertical)
            
        return ans
            