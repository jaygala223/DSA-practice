class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        
        int n=nums.size();
        if(n==0) return ans;
        
        sort(nums.begin(), nums.end());
        
        for(int i=0; i<n; i++){
            int target = -nums[i];
            
            int left=i+1, right= n-1;
            
            while(right > left){
                if(nums[right]+nums[left] == target) 
                {
                    ans.push_back({nums[i],nums[left],nums[right]});
                    int left_val = nums[left], right_val = nums[right];
                    
                    while(left<right && nums[left] == left_val) ++left;
                        
                    while(left<right && nums[right] == right_val) --right;
                }
                
                else if(nums[right]+nums[left] > target)
                    right--;
                
                else left++;
            }
            while(i+1 <n && nums[i+1] == nums[i]) ++i;
        }
        return ans;
    }
};