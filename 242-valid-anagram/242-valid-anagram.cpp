class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size();
        int m = t.size();
        
        if(s == t) return true;
        if(n != m) return false;
        
        vector<int> freq1(26,0);
        vector<int> freq2(26,0);
        
        for(int i=0; i<n; i++){
            freq1[s[i]-'a']++;
            freq2[t[i] - 'a']++;
        }
        
        return (freq1 == freq2);
    }
};