class Solution {
public:
    int f(int i, int sum, vector<int>& nums, vector<vector<int>> &dp){
        if(sum < 0) return 0;
        if(sum == 0) return 1;
        if(i == 0){
            return nums[0] == sum;
        }
        if(dp[i][sum] != -1) return dp[i][sum];
        
        int take = f(i-1, sum - nums[i], nums, dp);
        int notTake = f(i-1, sum, nums, dp);
        
        return dp[i][sum] = take or notTake;
    }
    
    
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        
        int totSum = accumulate(nums.begin(), nums.end(), 0);
        
        vector<vector<int>> dp(n+1, vector<int>(totSum + 1, -1));
        
        if(totSum % 2) return false;
        return f(nums.size()-1, totSum/2, nums, dp);
    }
};