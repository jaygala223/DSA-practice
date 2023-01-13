class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1
        
        ans = []
        
        def dfs(node):
            ans.append(node)
            indegree[node] -= 1
            
            for pre_req in graph[node]:
                indegree[pre_req] -= 1
                if indegree[pre_req] == 0:
                    dfs(pre_req)
            
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        
        return ans if len(ans) == numCourses else []