class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int n = nums.size();
        int left = 0, right = 0, sum = 0;
        
        for (int i : nums) sum += i;
        
        int k = sum - x, curSum = 0, ans = 0;
        bool found = false;
        while(right < n){
            curSum += nums[right];
            while(curSum>k and left <= right){
                    curSum -= nums[left];
                    left+=1;
                }
            
            if(curSum == k){
                found = true;
                ans = max(ans, right-left+1);   
            }    
            right++;
        }
        
        return found? n - ans: -1;
    }
};