class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = defaultdict(list)
        
        for p, c in roads:
            graph[p].append(c)
            graph[c].append(p)
            
        self.ans = 0
        
        def dfs(node, prev, persons = 1):
            for n in graph[node]:
                if n == prev: continue
                persons += dfs(n, node)
            
            self.ans += int(ceil(persons/seats) if node else 0)
            return persons
        
        dfs(0, -1)
        return self.ans
        
            