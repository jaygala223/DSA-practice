class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> mp;
        
        int left = 0, right = 0;
        int sum = 0, ans = 0;
        
        while(right < n){
                
            while(mp.find(nums[right]) != mp.end()){                    
                    sum -= nums[left];
                    mp.erase(nums[left]);
                    left+=1;
                }      
            
            sum += nums[right];
            mp[nums[right]] = right;
            ans = max(sum, ans);
            
            right++;
        }
        return ans;
    }
};