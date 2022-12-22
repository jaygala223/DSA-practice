class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj_list = defaultdict(list)
        
        #create adjacency map
        
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        ans = [-1] * n
        counts = [1] * n
        
        #for count of children of root of tree/graph
        self.root = 0
        
        def dfs_count(cur, parent, depth):
            curr_count = 1
            for child in adj_list[cur]:
                if child != parent:
                    curr_count += dfs_count(child, cur, depth+1)
                    self.root += (depth+1)
            counts[cur] = curr_count
            return curr_count
        
        dfs_count(0, -1, 0)
        
        def dfs_sum_dist(cur, parent, parent_sum):
            ans[cur] = parent_sum
            for child in adj_list[cur]:
                if child != parent:
                    dfs_sum_dist(child, cur, parent_sum + n - 2* counts[child])
                    
        dfs_sum_dist(0,-1, self.root)
        
        return ans
        
        