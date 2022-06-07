class Solution {
public:
    
    int partitionArray(vector<int>& nums, int k) {
        int ans = 0, start = 0;
        
        sort(nums.begin(), nums.end(), greater<int>());
        
        for(int i=1; i<nums.size(); i++){
            if(nums[start] - nums[i] > k){
                ans++;
                start = i;
            }
        }
        
        
        return ans+1;
    }
};