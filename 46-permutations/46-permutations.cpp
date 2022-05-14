class Solution {
public:
    void func(int i, int n, vector<vector<int>> &ans, vector<int> &arr){
        if(i > n-1){
            ans.push_back(arr);
            return;
        }
        
        for(int j=i; j<n; j++){
            swap(arr[i],arr[j]);
            func(i+1, n, ans, arr);
            swap(arr[j],arr[i]);
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        
        vector<vector<int>> ans;
        func(0, nums.size(), ans, nums);
        
        return ans;
    }
};