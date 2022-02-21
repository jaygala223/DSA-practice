class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        
        int ans = 0;
        int left = 0, right = 0;
        int farthest = 0;
        
        for(int i=0; i<n-1; i++){
            farthest = max(farthest, i+nums[i]);
            if(i==right){
                ans++;
                right = farthest;
            }
        }
        
        return ans;
    }
};