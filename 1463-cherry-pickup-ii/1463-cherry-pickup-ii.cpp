class Solution {
public:
    int func(int i, int j1, int j2, vector<vector<int>> &grid, vector<vector<vector<int>>> &dp){
    if(j1 < 0 or j2 < 0 or j1 > grid[0].size()-1 or j2 > grid[0].size()-1)
        return -1e8;
    if(i == grid.size()-1){
        if(j1 == j2) return grid[i][j1]; //koi bhi count karna
        return grid[i][j1] + grid[i][j2];
    }
    if(dp[i][j1][j2] != -1) return dp[i][j1][j2];
    //explore all paths
    int maxi = -1e8;
    for(int dj1=-1; dj1<=1; dj1++){
        for(int dj2=-1; dj2<=1; dj2++){
            if(j1 != j2){
                maxi = max(maxi, grid[i][j1] + grid[i][j2] + func(i+1, j1+ dj1, j2+dj2, grid, dp));
            }
            //koi ek lelo
            else maxi = max(maxi, grid[i][j1] + func(i+1, j1+ dj1, j2+dj2, grid, dp));
        }
    }
    return dp[i][j1][j2] = maxi;
}
    int cherryPickup(vector<vector<int>>& grid) {
        int r = grid.size();
        int c = grid[0].size();
        
        vector<vector<vector<int>>> dp(r, vector<vector<int>>(c, vector<int>(c,-1)));
        return func(0, 0, c-1, grid, dp);
    }
};