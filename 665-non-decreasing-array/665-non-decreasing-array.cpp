class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int n = nums.size();
        bool changed = false;
        
        if(n == 1 or n == 2) return true;
        
        for(int i=0; i<n-1; i++){
            if(nums[i] > nums[i+1]){
                if(changed) return false;
                
                if(i == 0 or nums[i+1] >= nums[i-1]) nums[i] = nums[i+1];
                
                else nums[i+1] = nums[i];
                
                changed = true;
            }
        }
        
        return true;
    }
};