class Solution {
public:
    int f(int i, vector<int> &nums, vector<int> &dp){
        if(i == 0) return nums[0];
        if(i < 0) return 0;
        if(dp[i] != -1) return dp[i];
        
        //int pick
        int pick = nums[i] + f(i-2, nums, dp);
        
        int notPick = 0 + f(i-1, nums, dp);
        
        return dp[i] = max(pick, notPick);
    }
    
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        
        dp[0] = nums[0];
        
        for(int i=1; i<nums.size(); i++){
            int pick = nums[i];
            
            if(i-2 >= 0) pick = nums[i] + dp[i-2];
        
            int notPick = 0 + dp[i-1];

            dp[i] = max(pick, notPick);
            
        }
        return dp[nums.size()-1];
        //return f(nums.size()-1, nums, dp);
    }
};