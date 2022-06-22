class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        priority_queue<int> hp(nums.begin(), nums.end());
        
        int cnt = 0;
        while(hp.size()){
            cnt++;
            if(cnt == k) return hp.top();
            hp.pop();
        }
        return 0;
    }
};