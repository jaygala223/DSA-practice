class Solution {
public:
    int maxScore(vector<int>& nums, int k) {
        int n = nums.size();
        
        int totSum = accumulate(nums.begin(), nums.end(), 0);
        
        if(k == n) return totSum;
        
        int left = 0, right = 0, len = n - k, mini = INT_MAX, subSum = 0;
        
        while(right < len){
            subSum += nums[right++];
        }
        mini = min(mini, subSum);
        while(right < n){
            subSum += nums[right++];
            subSum -= nums[left++]; 
            mini = min(mini, subSum);
        }
        
        
        //cout<<mini<<" ";
        return totSum - mini;
    }
};