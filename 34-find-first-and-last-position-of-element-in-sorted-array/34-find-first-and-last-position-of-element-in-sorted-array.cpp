class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        
        int cnt=0, cnt2 = 0, f=-1, l=-1;
        int i = 0;
        while(i<n){
            if(nums[i] == target and cnt == 0) {
                f = i;
                cnt++;
            }
            if(nums[n-i-1] == target and cnt2 == 0) {
                l=n-i-1;
                cnt2++;
            }

            if(f!=-1 and l!=-1) break;       
            i++;
        }
        
        
        vector<int> ans(2);
        ans[0] = f;
        ans[1] = l;
        return ans;
    }
};