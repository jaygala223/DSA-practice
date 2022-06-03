class Solution {
public:
    int func(int i, int j, int m, vector<vector<int>> &triangle, vector<vector<int>> &dp){
        if(i == m-1) return triangle[i][j];
        
        if(dp[i][j] != -1) return dp[i][j];
        
        int down = triangle[i][j] + func(i+1, j, m, triangle, dp);
        int diag = triangle[i][j] + func(i+1, j+1, m, triangle,dp);
        
        return dp[i][j] = min(down, diag);
    }
    
    
    int minimumTotal(vector<vector<int>>& triangle) {
        int m = triangle.size();
        
        vector<vector<int>> dp(m, vector<int>(m,0));
        
        for(int j=0;j<m; j++) dp[m-1][j] = triangle[m-1][j];
        
        for(int i=m-2; i>=0; i--){
            for(int j=0; j<=i; j++){
                int down = triangle[i][j] + dp[i+1][j];
                int diag = triangle[i][j] + dp[i+1][j+1];
                dp[i][j] = min(down, diag);
            }
        }
        
        return dp[0][0];
        //return func(0, 0, m, triangle, dp);
    }
};