class Solution:
    
    #top down memoized
#         def helper(row, col, grid, dp):
#             if row < 0 or col < 0 or grid[row][col] == 1: return 0
            
#             if row == 0 and col == 0: return 1
#             if (row,col) in dp: return dp[(row, col)]
            
#             left = helper(row, col-1, grid, dp)
#             up = helper(row-1, col, grid, dp)
            
#             dp[(row, col)] = left+up
#             return dp[(row, col)]
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        #dp = {}       
        
        #bottom up - tabulated
        #dp[(0,0)] = 1
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        
        dp = [[0]* n for _ in range(m)]
        dp[0][0] = 1
        
        
        for i in range(1,m):
            dp[i][0] = 1 if obstacleGrid[i][0]==0 and dp[i-1][0]==1 else 0
            
        for j in range(1,n):
            dp[0][j] = 1 if obstacleGrid[0][j]==0  and dp[0][j-1]==1 else 0
        
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] != 1: 

                    left = dp[row][col-1]
                    up = dp[row-1][col]

                    dp[row][col] = left+up
        
        
        
        return dp[m-1][n-1]