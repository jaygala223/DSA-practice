class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
        int rule1 = 0;
        int rule2 = 0;
        if(nums.size()==1) {
            return 0;
        }
        vector<int>nums2 = nums;
        for(int i = 0 ; i < nums.size() ; i=i+2) {
            if(i==0) {
                if(nums[0]<=nums[1]) {
                    int diff = nums[1] - nums[0] + 1;
                    rule1 += diff;
                    nums[1] -= diff;
                }
            }
            else if(i==nums.size()-1) {
                if(nums[i]<=nums[i-1]) {
                    int diff = nums[i-1] - nums[i] + 1;
                    rule1 += diff;
                    nums[i-1] -= diff;
                }
            }
            else{
                if(nums[i]<=nums[i-1]) {
                    int diff = nums[i-1] - nums[i] + 1;
                    rule1 += diff;
                    nums[i-1] -= diff;
                }
                if(nums[i]<=nums[i+1]) {
                    int diff =nums[i+1] - nums[i] + 1;
                    rule1 += diff;
                    nums[i+1] -= diff;
                }
            }
        }
        
        
        for(int i = 1 ; i < nums2.size() ; i=i+2) {
            if(i==nums.size()-1) {
                if(nums2[i]<=nums2[i-1]) {
                    int diff = nums2[i-1] - nums2[i] + 1;
                    rule2 += diff;
                    nums2[i-1] -= diff;
                }
            }
            else{
                if(nums2[i]<=nums2[i-1]) {
                    int diff = nums2[i-1] - nums2[i] + 1;
                    rule2 += diff;
                    nums2[i-1] -= diff;
                }
                if(nums2[i]<=nums2[i+1]) {
                    int diff =nums2[i+1] - nums2[i] + 1;
                    rule2 += diff;
                    nums2[i+1] -= diff;
                }
            }
        }
        return min(rule1,rule2);
    }
};