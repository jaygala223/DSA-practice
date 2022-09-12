class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        #dp = [[-1]*n]*m
        
        dp = {}
                
        def helper(row, col, dp):
            print(dp)
            #this is one way to reach the dest
            if row == 0 and col == 0: return 1

            if row < 0 or col < 0: return 0

            if (row,col) in dp: return dp[(row,col)]

            left = helper(row, col-1, dp)
            up = helper(row-1, col, dp)
            dp[(row,col)] = left+up
            return dp[(row,col)]
        
        return helper(m-1, n-1, dp)