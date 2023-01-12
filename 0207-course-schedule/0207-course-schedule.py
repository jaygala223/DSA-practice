class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        visited = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True