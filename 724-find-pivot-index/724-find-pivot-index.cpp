class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size(), sum=0, total=0;
        
        for(auto num: nums) total += num;
        
        for(int i=0; i<n; i++){
            if(sum*2 == total - nums[i]) return i;
            sum += nums[i];
        }
        
        return -1;
    }
};