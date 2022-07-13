class Solution {
public:
    bool f(int i, int k, int currSum, int tar, vector<int>& nums, vector<int>& used){
        if(k == 1) return true;
        if(i >= nums.size()) return false;
        if(currSum == tar) return f(0, k-1, 0, tar, nums, used);
        
        for(int j=i; j<nums.size(); j++){
            if(used[j] or nums[j] + currSum > tar) continue;
            
            used[j] = 1;
            
            if(f(j+1, k, currSum + nums[j], tar, nums, used)) return true;
            
            //backtrack
            used[j] = 0;
        }
        return false;
    }
    
    bool makesquare(vector<int>& nums) {
        int n = nums.size();
        
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(sum%4) return false;
        
        sort(nums.begin(), nums.end(), greater<int>());
        
        int sideLen = sum/4;
        vector<int> used(n, 0);
        return f(0, 4, 0, sideLen, nums, used);
    }
};