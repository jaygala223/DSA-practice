class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def dfs(node, visited, distances, dist):
            if node != -1 and node not in visited:
                visited.add(node)
                distances[node] = dist
                dfs(edges[node], visited, distances, dist + 1)
        
        distFromN1, distFromN2 = [-1]*len(edges), [-1]*len(edges)
        
        dfs(node1, set(), distFromN1, 0)
        dfs(node2, set(), distFromN2, 0)
        
        ans = 1e9
        result = -1
        
        for i in range(len(edges)):
            if distFromN1[i] != -1 and distFromN2[i] != -1:
                if max(distFromN1[i], distFromN2[i]) < ans:
                    ans = max(distFromN1[i], distFromN2[i])
                    result = i
        return result