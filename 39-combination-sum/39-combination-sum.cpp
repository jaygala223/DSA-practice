class Solution {
public:
    void func(int i, int n, int target, vector<int> &nums, vector<int> &ds, vector<vector<int>> &ans){
        
        if(i>n-1){
            if(target == 0) ans.push_back(ds);
            return;
        }
        
        //same number pick karke wapas ispe hi aao
        if(nums[i] <= target) {
            ds.push_back(nums[i]);
            func(i, n, target - nums[i], nums, ds, ans);
            ds.pop_back();
        }
        
        
        func(i+1, n, target, nums, ds, ans);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> ds;
        vector<vector<int>> ans; 
        func(0, candidates.size(), target, candidates, ds, ans);
        return ans;
    }
};