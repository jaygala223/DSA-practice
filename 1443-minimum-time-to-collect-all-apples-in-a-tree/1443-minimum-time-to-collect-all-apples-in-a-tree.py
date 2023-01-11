class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        tree = defaultdict(list)
        
        for p,c in edges:
            #twice because undirected hai
            tree[p].append(c)
            tree[c].append(p)
            
        def dfs(node, parent):
            ans = 0
            
            for nei in tree[node]:
                #taki ulta na chala jaaye galti se
                if nei != parent:
                    ans += dfs(nei, node)
                    
                #agar neeche apple hai i.e. ans!=0 to uss raste par jana padega... athva node khud hi apple wala hai to jan hi padega yaha
            if ans or hasApple[node]:
                ans += 2
                
            return ans
        
        return max(dfs(0,-1)-2,0)