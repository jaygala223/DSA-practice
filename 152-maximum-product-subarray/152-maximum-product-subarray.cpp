class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
        int ans, currMax, currMin;
        ans = currMax = currMin = nums[0];
        
        for(int i=1; i<nums.size(); i++){
            int curr = nums[i];
            if(curr < 0) swap(currMax, currMin);
            
            currMin = min(curr, currMin*curr);
            currMax = max(curr, currMax*curr);
            
            cout<<"min is = "<<currMin<<endl;
            cout<<"max is = "<<currMax<<endl;
            
            ans = max(ans, currMax);
        }
        
        return ans;
    }
};