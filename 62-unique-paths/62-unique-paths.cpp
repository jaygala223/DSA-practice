class Solution {
public:
    int func(int row, int column, int m, int n, vector<vector<int>> &dp){
        if(row == 0 and column == 0){
            return 1;
        }
        else if(row < 0 or column < 0) return 0;
        else if(dp[row][column] != -1) return dp[row][column];
        
        //since we're going top down dp
        int up = func(row-1, column, m, n, dp);
        int left = func(row, column-1, m, n, dp);
        
        return dp[row][column] = up + left;
         
    }
    
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m+1, vector<int>(n+1, -1));
        
        //tabulization, bottom to up DP
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i == 0 and j == 0) {
                    dp[i][j] = 1;
                    continue;
                }
                int up = 0;
                if(i-1>=0) up = dp[i-1][j];
                int left = 0;
                if(j-1>=0) left = dp[i][j-1];
                dp[i][j] = left + up;
            }
        }
        return dp[m-1][n-1];
    }
};