class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        
        int i = n-1;
        int goal = n-1;
        
        while(i--){
          if(i + nums[i] >= goal){
              goal = i;
          }  
        }
        return goal==0;
    }
};