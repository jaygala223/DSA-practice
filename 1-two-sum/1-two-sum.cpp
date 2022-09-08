class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> map1;
        vector<int> ans;
        
        for(int i=0; i<=nums.size(); i++){
            int subtraction = target - nums[i];
            
            //agar mil gaya to 
            if(map1.find(subtraction) != map1.end()){ 
                return {map1[subtraction], i};
            
             }       
            map1[nums[i]] = i;
        
        }
        return ans;
        
    }
};