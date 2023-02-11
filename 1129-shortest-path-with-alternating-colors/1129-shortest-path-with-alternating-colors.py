class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        #TC: O(N*(v+e)) -> BFS traversal for n nodes -> O(N*V*E)
        #SC: O(V+E) for graph
        
        d = [defaultdict(list), defaultdict(list)]
        for a, b in redEdges: d[0][a] += (b, 0),
        for a, b in blueEdges: d[1][a] += (b, 1),
            
        def bfs(tar):
            q = [(0, 0, 1), (0, 0, 0)]
            seen = [defaultdict(int), defaultdict(int)]
            for cur, h, p in q:
                if cur == tar: return h
                for n, c in d[1-p][cur]:
                    if not seen[1-p][n]:
                        q.append((n, h+1, c))
                        seen[1-p][n] = 1
            return -1
        
        return [i and bfs(i) for i in range(n)]
                    