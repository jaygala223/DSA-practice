class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        self.dfs(graph, [0], 0, res)
        
        return res
        
        
    def dfs(self, graph, cur_res, cur_node, res):
        if cur_node == len(graph)-1:
            res.append(list(cur_res))
        
        for node in graph[cur_node]:
            cur_res.append(node)
            self.dfs(graph, cur_res, node, res)
            cur_res.pop()