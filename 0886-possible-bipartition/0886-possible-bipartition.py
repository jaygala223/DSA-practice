class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        
        def isBipartite(adj_list, node, n, color):
            q = []
            q.append(node)
            color[node] = 1
            
            while q:
                curr = q[0]
                q.pop(0)
                for ele in adj_list[curr]:
                    if color[ele] == color[curr]: return False
                    if color[ele] == -1:
                        q.append(ele)
                        color[ele] = 1 - color[curr]
            return True
        
        adj_list = defaultdict(list)
        
        for item in dislikes:
            a, b = item[0], item[1]
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        color = [-1] * (n+1)
        
        for i in range(1, n+1):
            if color[i] == -1:
                if not isBipartite(adj_list, i, n, color):
                    return False
            
        return True