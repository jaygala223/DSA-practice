class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = [False]*n
        
        def dfs(i):
            visited[i] = True
            
            for j in range(len(visited)):
                if i!=j and isConnected[i][j] and not visited[j]:
                    dfs(j)
                    
        ans = 0
        for i in range(len(visited)):
            if not visited[i]:
                dfs(i)
                ans += 1
                
        return ans