class Solution {
public:
    int robby(vector<int>&nums) {
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
    
    
    int rob(vector<int> &nums) {
        if(nums.size() == 1) return nums[0];
        //if(nums.size() == 2) return max(nums[0], nums[1]);
        
        vector<int> temp1(nums.begin(), nums.end()-1), temp2(nums.begin()+1, nums.end());
        
        return max(robby(temp1), robby(temp2));
        
    }
};