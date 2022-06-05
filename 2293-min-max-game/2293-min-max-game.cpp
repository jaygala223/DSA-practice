class Solution {
public:
    int minMaxGame(vector<int>& nums) {
        int n = nums.size();
        
        while(n != 1){
            vector<int> temp;
            bool flag = true;
            for(int i=0; i<nums.size(); i+=2){
                if(flag){
                    temp.push_back(min(nums[i], nums[i+1]));
                    flag = false;
                }
                else{
                    temp.push_back(max(nums[i], nums[i+1]));
                    flag = true;
                }
            }
                
            n = temp.size();
            nums = temp;
        }
        
        return nums[0];
    }
};