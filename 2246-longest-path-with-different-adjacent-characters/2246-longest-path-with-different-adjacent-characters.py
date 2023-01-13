class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        #refer: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/discuss/1955433/JavaC%2B%2BPython-DFS-on-Tree
        tree = defaultdict(list)
        
        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
        
        self.ans = 1
        
        def func(node):
            if node not in tree: return 1
            
            res = 1
            
            for nei in tree[node]:
                length = func(nei)
                if s[node] != s[nei]:
                    self.ans = max(self.ans, length + res)
                    res = max(res, length + 1)
            return res
        
        func(0)
        return self.ans