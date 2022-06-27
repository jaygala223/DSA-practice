class Solution {
public:
    int maxScore(vector<int>& nums, int k) {
        int n = nums.size();
        
        int totSum = accumulate(nums.begin(), nums.end(), 0);
        
        if(k == n) return totSum;
        
        int len = n - k, mini = INT_MAX, subSum = 0;
        queue<int> q;
        
        for(int i=0; i<n; i++){
            subSum += nums[i];
            q.push(nums[i]);
            if(q.size() == len) mini = min(subSum, mini);
            
            else if(q.size() > len){
                subSum -= q.front();
                q.pop();
                mini = min(subSum, mini);
            }
            
        }
        cout<<mini<<" ";
        return totSum - mini;
    }
};