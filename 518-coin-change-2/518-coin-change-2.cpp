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
        vector<vector<int>> dp(n, vector<int>(amount+1, -1));
        
        return f(n-1, amount, coins, dp);
    }
};