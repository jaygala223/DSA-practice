class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda : defaultdict(set))
        
        red, blue = 0, 1
        
        for p, c in redEdges:
            graph[p][red].add(c)
        for p, c in blueEdges:
            graph[p][blue].add(c)
        
        
        ans = [1e9] * n
        
        r, b = 0, 1
        
        #start karenge zero se
        q = [(0, red), (0, blue)]
        level = -1
        
        while q:
            #zero ke liye level ka ans zero hojayega
            level += 1
            sz = len(q)
            for i in range(sz):
                node, color = q.pop(0)
                ans[node] = min(level, ans[node])
                opp_color = color^1 #xor
                
                neighbors = graph[node][opp_color]
                
                for child in list(neighbors):
                    graph[node][opp_color].remove(child)
                    q.append((child, opp_color))
        
        return [x if x != 1e9 else -1 for x in ans]
                    