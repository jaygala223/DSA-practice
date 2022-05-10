class Solution {
public:
    void func(int i, int target, vector<int> &ds, vector<vector<int>> &ans, vector<int> &arr){
        if(target == 0){ 
            ans.push_back(ds);
            return;
        }
        
        for(int ind=i; ind<arr.size(); ind++){
            
            //agar prev element same h to aage badho
            if(ind>i && arr[ind] == arr[ind-1]) continue;
            
            //agar ye number khud bada hua to usse aage ke bhi bade honge... 
            //so no need to check
            if(arr[ind] > target) break;
            
            ds.push_back(arr[ind]);
            func(ind+1, target - arr[ind], ds, ans, arr);
            ds.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> ds;
        vector<vector<int>> ans;
        
        func(0, target, ds, ans, candidates);
        
        return ans;
    }
};