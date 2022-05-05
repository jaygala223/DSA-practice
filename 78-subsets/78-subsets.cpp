class Solution {
public:
    vector<vector<int>> subs;
    
    void func(int i, int n, vector<int> &nums, vector<int> &sub){
        if(i>n-1){
            subs.push_back(sub);
            return;
        }    
        sub.push_back(nums[i]);
        func(i+1, n, nums, sub);
        sub.pop_back();
        func(i+1, n, nums, sub);
    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<int> sub;
        func(0, n, nums, sub);
        return subs;
    }
};