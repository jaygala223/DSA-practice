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
        
        vector<vector<int>> dp(m, vector<int>(m,-1));
        
        return func(0, 0, m, triangle, dp);
    }
};