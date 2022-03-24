class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int ans = *max_element(nums.begin(), nums.end());
        cout<<ans;
        
        int currMin = 1, currMax = 1;
        
        for(auto item: nums){
            int temp = currMin*item;
            
            currMin = min(item*currMax, currMin*item);
            currMin = min(item, currMin);
            
            currMax = max(currMax*item, temp);
            currMax = max(item, currMax);
            
            ans = max(ans, currMax);
        }
        return ans;
    }
};