class Solution {
public:
    int maxScore(vector<int>& nums, int k) {
        int n = nums.size();
        
        int lSum = 0, rSum = 0;
        
        for(int i=0; i<k; i++){
            lSum += nums[i];
        }
        
        int maxi = lSum;
        for(int i=0; i<k; i++){
            rSum += nums[n - i - 1];
            lSum -= nums[k - i - 1];
            maxi = max(maxi, rSum + lSum);
        }
        
        return maxi;
    }
};