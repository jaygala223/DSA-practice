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
    
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        
        int sum = accumulate(nums.begin(),nums.end(),0);
        if(sum % k) return false;
        
        int target = sum/k;
        vector<int> used(nums.size(), 0);
        sort(nums.begin(), nums.end(), greater<int>());
        return f(0, k, 0, target, nums, used);
    }
};