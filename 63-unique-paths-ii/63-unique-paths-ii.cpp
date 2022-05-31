class Solution {
public:
    int func(int i, int j, vector<vector<int>>& grid, vector<vector<int>> &dp){
        if(i == 0 and j == 0) {
            if(grid[i][j] == 0) return 1;
            else return 0;
        }
        else if(i < 0 or j < 0) return 0;
        else if(grid[i][j] == 1) return 0;
        else if(dp[i][j] != -1) return dp[i][j];
        
        //going top down
        int left = func(i, j-1, grid, dp);
        int up = func(i-1, j, grid, dp);
        
        return dp[i][j] = left + up;
    }
    
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return func(m-1, n-1, obstacleGrid, dp);
    }
};