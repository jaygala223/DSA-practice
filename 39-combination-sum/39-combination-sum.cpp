class Solution {
public:
    void func(int i, int n, int sum, int target, vector<int> &nums, vector<int> &ds, vector<vector<int>> &ans){
        
        if(i>n-1){
            if(sum == target) ans.push_back(ds);
            return;
        }
        
        sum += nums[i];
        ds.push_back(nums[i]);
        
        //same number pick karke wapas ispe hi aao
        if(sum <= target) {
            func(i, n, sum, target, nums, ds, ans);
        }
        
        //same number pick karke aage badho
        //if(sum <= target) func(i+1, n, sum, target, nums, ds, ans);
        
        ds.pop_back();
        sum -= nums[i];
        
        if(sum <= target) func(i+1, n, sum, target, nums, ds, ans);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> ds;
        vector<vector<int>> ans; 
        func(0, candidates.size(), 0, target, candidates, ds, ans);
        return ans;
    }
};