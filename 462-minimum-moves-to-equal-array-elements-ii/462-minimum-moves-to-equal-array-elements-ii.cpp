class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int n = nums.size();
        
        sort(nums.begin(), nums.end());
        
        int median = 0, ans = 0;
        if(n%2 == 0) median = (n/2) - 1;
        else median = ((n+1)/2) - 1;
        cout<<median;
        for(int i=0; i<n; i++){
            if(i == median) continue;
            ans += abs(nums[median] - nums[i]);
        }
        return ans;
    }
};