class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = {}
        
        def helper(row, col, grid, dp):
            if row < 0 or col < 0 or grid[row][col] == 1: return 0
            
            if row == 0 and col == 0: return 1
            if (row,col) in dp: return dp[(row, col)]
            
            left = helper(row, col-1, grid, dp)
            up = helper(row-1, col, grid, dp)
            
            dp[(row, col)] = left+up
            return dp[(row, col)]
        
        return helper(m-1, n-1, obstacleGrid, dp)