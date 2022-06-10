class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0, n = s.size();
        unordered_map<char, int> mp;
        int left = 0, right = 0;
        
        while(left < n and right < n){
            
            //agar repeating element mil gaya to
            if(mp.find(s[right]) != mp.end()){
                left = max(left, mp[s[right]]+1);
            }
            mp[s[right]] = right;
            int current = right - left + 1;
            ans = max(ans, current);
            right++;
        }
        
        return ans;
    }
};