class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0;
        int curr = 0;
        
        for(int n: nums){
            if(n == 1){
                curr++;
                ans = max(ans, curr);
            }
            else curr=0;
        }
        return ans;
    }
};