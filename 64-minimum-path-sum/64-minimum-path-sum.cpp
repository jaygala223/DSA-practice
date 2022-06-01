class Solution {
public:
    int func(int i, int j, int sum, vector<vector<int>> &grid, vector<vector<int>> &dp){
        if(i == 0 and j == 0){
            return grid[0][0]; 
        }
        if(i < 0 or j < 0) return 201;
        if(dp[i][j] != -1) return dp[i][j];
        
        //top down hai isiliye
        int up = grid[i][j] + func(i-1, j, sum, grid, dp);
        int left = grid[i][j] + func(i, j-1, sum, grid, dp);
        
        return dp[i][j] = min(left, up);
    }
    
    int minPathSum(vector<vector<int>>& grid) {
        
        
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n,0));
    
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i == 0 and j == 0) {
                    dp[i][j] = grid[0][0];
                    continue;
                }
                
                int left = 201, up = 201;
                
                if(j>0) left = grid[i][j] + dp[i][j-1];
                if(i>0) up =  grid[i][j] + dp[i-1][j];
                
                dp[i][j] = min(left, up);
            }
        }
        return dp[m-1][n-1];
    }
};