class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        
        zeros = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_i, start_j = (i, j)
                if grid[i][j] == 0 or grid[i][j] == 1:
                    zeros += 1

        def dfs(i, j, zeros):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] < 0:
                return 0
            if grid[i][j] == 2:
                self.ans += zeros == 0
                return
            
            dirs = [(-1,0), (0,1), (0,-1), (1,0)]
            
            grid[i][j] = -1
            for row,col in dirs:
                dfs(i + row, j + col, zeros-1)
            grid[i][j] = 0
            
        dfs(start_i, start_j, zeros)
        return self.ans
            