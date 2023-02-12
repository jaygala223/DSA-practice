class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        #TC: O(V+E) -> dfs traversal
        #SC: O(V+E) -> graph + recursive stack space (not counting it in sc)
        
        graph = defaultdict(list)
        
        for p, c in roads:
            graph[p].append(c)
            graph[c].append(p)
            
        self.ans = 0
        
        def dfs(node, prev, persons = 1):
            for n in graph[node]:
                if n == prev: continue
                persons += dfs(n, node)
            
            #har node pe jitni gadi aage badh rahi hai utna unit fuel use hoga and wohi ans hoga
            self.ans += int(ceil(persons/seats) if node else 0)
            return persons
        
        dfs(0, -1)
        return self.ans
        
            