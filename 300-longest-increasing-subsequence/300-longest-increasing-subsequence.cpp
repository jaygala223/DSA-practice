class Solution {
public:
    int f(int i, vector<int>& nums, int prev, vector<vector<int>>& dp){
        if(i == nums.size()){
            return 0;
        }
        if(dp[i][prev+1] != -1) return dp[i][prev];
        
        //take
        int take = 0;
        if(prev == -1) take = 1 + f(i+1, nums, i, dp);
        else if(nums[i] > nums[prev]) take = 1 + f(i+1, nums, i, dp);
        
        int notTake = f(i+1, nums, prev, dp);
        
        return dp[i][prev+1] = max(take, notTake);
    }
    
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        
        for(int i=n-1; i>=0; i--){
            for(int prev=i-1; prev>=-1; prev--){
                
                int take = 0;
                if(prev == -1) take = 1 + dp[i+1][i+1];
                else if(nums[i] > nums[prev]) take = 1 + dp[i+1][i+1];

                int notTake = dp[i+1][prev+1];

                dp[i][prev+1] = max(take, notTake);
            }
        }
        
        //coordinate shift
        return dp[0][-1+1];
    }
};