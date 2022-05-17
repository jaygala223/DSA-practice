class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
         int even = 0, odd = 0, n = nums.size();
    //for odd
        for(int i=1; i < n; i+= 2){
            int minVal = min(nums[i-1], i+1 < n ? nums[i+1] : 1001);
            if(minVal <= nums[i])
                odd += (nums[i]-minVal+1);
        }
    // For Even
        for(int i=0; i < n; i+= 2){
            int minVal = min(i > 0 ? nums[i-1] : 1001, i+1 < n ? nums[i+1] : 1001);
            
            if(minVal <= nums[i]) even += (nums[i]-minVal+1);
               
        }
        return min(even,odd);
    }
};