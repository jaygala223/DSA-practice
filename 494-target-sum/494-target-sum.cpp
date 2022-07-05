class Solution {
public:
    int f(vector<int> &nums, int tar){
        int n = nums.size();
        vector<int> prev(tar+1, 0), cur(tar+1, 0);
        
        if(nums[0] == 0) prev[0] = 2;
        else prev[0] = 1;
        
        if(nums[0] != 0 and nums[0] <= tar) prev[nums[0]] = 1;
        for(int ind=1; ind<n; ind++){
            for(int sum=0; sum<=tar; sum++){
                int notTake = prev[sum];
                int take = 0;
                if(nums[ind] <= sum) take = prev[sum - nums[ind]];
                
                cur[sum] = notTake + take;
            }
            prev = cur;
        }
        return prev[tar];
    }
    
    
    int findTargetSumWays(vector<int>& nums, int target) {
        int tot = 0;
        for(auto item: nums) tot += item;
        if(tot - target < 0 || (tot - target) % 2) return false;
        return f(nums, (tot - target) /2);
    }
};