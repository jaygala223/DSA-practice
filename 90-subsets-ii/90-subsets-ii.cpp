class Solution {
public:
    void func(int i, int n, vector<int> &ds, vector<int> &arr, vector<vector<int>> &ans){
        
        //if(i>n-1) return;
        
        ans.push_back(ds);
        
        for(int ind=i; ind<arr.size(); ind++){
            
            //agar prev element same h to aage badho
            if(ind>i && arr[ind] == arr[ind-1]) continue;
            
            //agar ye number khud bada hua to usse aage ke bhi bade honge... 
            //so no need to check
            //if(arr[ind] > target) break;
            
            ds.push_back(arr[ind]);
            func(ind+1, n, ds, arr, ans);
            ds.pop_back();
        }
    }
    
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        vector<int> ds;
        func(0, nums.size(), ds, nums, ans);
        
        return ans;
    }
};