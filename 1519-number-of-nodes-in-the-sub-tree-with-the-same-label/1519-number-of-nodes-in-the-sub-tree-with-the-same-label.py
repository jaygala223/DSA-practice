class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        ans = [-1] * n
        tree = defaultdict(list)
        
        for parent, child in edges:
            tree[parent].append(child)
            tree[child].append(parent)
        
        def dfs(node, parent):
            counter = collections.Counter()
            
            for nei in tree[node]:
                if nei != parent:
                    counter += dfs(nei, node)
            
            counter[labels[node]] += 1
            ans[node] = counter[labels[node]]
            
            return counter

        dfs(0,-1)
        return ans