class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int n = nums.size();
        
        int median = 0, ans = 0;
        if(n%2 == 0) median += (n/2)-1;
        else median += ((n+1)/2)-1;
        
        sort(nums.begin(), nums.end());
        
        for(int i=0; i<n; i++){
            ans += abs(nums[median] - nums[i]);
        }
        return ans;
    }
};