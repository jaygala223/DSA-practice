class Solution {
public:
    int f(int i, int k, vector<int>& nums, vector<int> &dp){
        
        //base
        if(i == 0) return nums[0];
        if(dp[i] != -1) return dp[i];
        
        int jump = INT_MIN;
        for(int j=1; j<=k; j++){
            int newJump = nums[i];
            if(i-j >= 0) newJump += f(i-j, k, nums, dp);
            jump = max(jump, newJump);
        }
        return dp[i] = jump;
    }
    
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        
        deque<int> q;
        q.push_back(0);
        
        for(int i=1; i<n; i++){
            if(q.front() + k < i) q.pop_front();
            
            nums[i] += nums[q.front()];
            
            while(!q.empty() and nums[q.back()] <= nums[i]) q.pop_back();
            
            q.push_back(i);
        }
        
        return nums.back();
        //return f(nums.size()-1, k, nums, dp);
    }
};