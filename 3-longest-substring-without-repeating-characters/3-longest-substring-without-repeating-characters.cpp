class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        
        unordered_map<int, int> mp;
        int left = 0, right = 0, ans = 0;
        
        while(left < n and right < n){
            if(mp.find(s[right]) != mp.end()){
                left = max(left, mp[s[right]] + 1);
            }
            
            mp[s[right]] = right;
            int currLen = right - left + 1;
            ans = max(ans, currLen);
            right++;
        }
        
        return ans;
    }
};