class Solution {
public:
    int minDeletions(string s) {
        int n = s.size(), ans = 0;
        vector<int> freq(26);
        
        //sort(s.begin(), s.end());
        for(auto ch: s) freq[ch - 'a']++;
        
        sort(freq.begin(), freq.end(), greater<int>());
        
        int maxFreq = freq[0];
        
        for(auto it: freq){
            if(it > maxFreq){
                if(maxFreq > 0) ans += it - maxFreq;
                else ans += it;
            }
            maxFreq = min(maxFreq - 1, it-1);
        }
            
        return ans;
    }
};