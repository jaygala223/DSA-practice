class Solution {
public:
    int f(int i, vector<int>& nums, int prev, vector<vector<int>>& dp){
        if(i == nums.size()){
            return 0;
        }
        if(dp[i][prev] != -1) return dp[i][prev];
        
        //take
        int take = 0;
        if(prev == nums.size()+2) take = 1 + f(i+1, nums, i, dp);
        else if(nums[i] > nums[prev]) take = 1 + f(i+1, nums, i, dp);
        
        int notTake = f(i+1, nums, prev, dp);
        
        return dp[i][prev] = max(take, notTake);
    }
    
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n+3, vector<int>(n+3, -1));
        return f(0, nums, n+2, dp);
    }
};