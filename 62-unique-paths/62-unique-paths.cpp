class Solution {
public:
    //int ans = 0;
    int bfs(int row, int column, int m, int n, vector<vector<int>> &dp){
        if(row == 0 and column == 0){
            return 1;
        }
        else if(row < 0 or column < 0) return 0;
        else if(dp[row][column] != -1) return dp[row][column];
        
        //since we're going bottom up dp
        int up = bfs(row-1, column, m, n, dp);
        int left = bfs(row, column-1, m, n, dp);
        
        return dp[row][column] = up + left;
         
    }
    
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m+1, vector<int>(n+1, -1));
        return bfs(m-1,n-1,m,n, dp);
    }
};