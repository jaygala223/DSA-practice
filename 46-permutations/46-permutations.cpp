class Solution {
public:
    void func(int n, vector<int> &map, vector<int> &ds, vector<int> &arr, vector<vector<int>> &ans){
        if(ds.size() == n){
            ans.push_back(ds);
            return;
        }
        
        for(int j=0; j<n; j++){
            if(map[j] == 0){
                ds.push_back(arr[j]);
                map[j] = 1;
                func(n, map, ds, arr, ans);
                ds.pop_back();
                map[j] = 0;    
            }
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> ds;
        vector<int> map(nums.size(),0);
        func(nums.size(), map, ds, nums, ans);
        return ans;
    }
};