class Solution {
public:
    int f(int i, int t, vector<int> &coins, vector<vector<int>>& dp){
        if(i == 0){
            if(t%coins[0] == 0) return t/coins[0];
            return 1e9;
        }
        if(dp[i][t] != -1) return dp[i][t];
        
        int take = 1e9;
        if(coins[i] <= t) take = 1 + f(i, t - coins[i], coins, dp);
        
        int notTake = 0 + f(i-1, t, coins, dp);
        
        return dp[i][t] = min(take, notTake);
    }
    int coinChange(vector<int>& coins, int t) {
        int n = coins.size();
        
        if(t == 0) return 0;
        
        vector<vector<int>> dp(n+1, vector<int>(t+1, 0));
        
        for(int tar=0; tar<=t; tar++){
            if(tar%coins[0] == 0) dp[0][tar] = tar/coins[0];
            else dp[0][tar] = 1e9;
        }
        
        for(int i=1; i<n; i++){
            for(int tar=0; tar<=t; tar++){
                int take = 1e9;
                if(coins[i] <= tar) take = 1 + dp[i][tar - coins[i]];

                int notTake = 0 + dp[i-1][tar];

                dp[i][tar] = min(take, notTake);
            }
        }
        
        int ans = dp[n-1][t];
        if(ans >= 1e9) return -1;
        return ans;
    }
};