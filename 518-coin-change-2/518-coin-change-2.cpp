class Solution {
public:
    int f(int i, int amt, vector<int>& coins, vector<vector<int>> &dp){
        //base
        //if(amt == 0) return 1;
        if(i == 0){
            return (amt % coins[0] == 0);
        }
        if(dp[i][amt] != -1) return dp[i][amt];
        
        int take = 0;
        if(coins[i] <= amt) take = f(i, amt - coins[i], coins, dp);
        
        int notTake = f(i-1, amt, coins, dp);
        
        return dp[i][amt] = notTake + take;
    }
    
    int change(int amount, vector<int>& coins) {
        int n = coins.size();
        vector<vector<int>> dp(n+1, vector<int>(amount+1, 0));
        
        for(int amt=0; amt<=amount; amt++){
            if(amt % coins[0] == 0) dp[0][amt] = 1;
        }
        
        for(int i=1; i<n; i++){
            for(int amt=0; amt<=amount; amt++){
                int take = 0;
                if(coins[i] <= amt) take = dp[i][amt - coins[i]];

                int notTake = dp[i-1][amt];

                dp[i][amt] = notTake + take;
            }
        }
        
        return dp[n-1][amount];
    }
};