class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        #TC: O(n^m) -> for traversal and BFS
        #SC: O(n) -> linear for Queue
        
        m, n = len(grid), len(grid[0])
        
        q = []
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    q.append((i,j))
        
        #if no land or all land return -1
        if len(q) == m*n or len(q) == 0:
            return -1
        
        ans = 0
        
        dx, dy = [-1,0,1,0], [0,1,0,-1]
        
        while q:
            ans += 1
            
            size = len(q)
            
            while size:
                x, y = q[0]
                q.pop(0)
                
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    
                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == 0:
                        q.append((new_x, new_y))
                        #mark visited
                        grid[new_x][new_y] = 1
                
                size -= 1
        
        return ans-1