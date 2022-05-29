class Solution {
public:
    int rearrangeCharacters(string s, string target) {
        if(target.size() > s.size()) return 0;
       
        vector<int> freq1(26,0);
        vector<int> freq2(26,0);
        
        for(auto ch: s){
            freq1[ch - 'a']++;
        }
        
        for(auto ch: target){
            freq2[ch - 'a']++;
        }
        
        int cnt = INT_MAX;
        for(int i=0; i<26; i++){
            if(freq2[i] > 0){
                cnt = min(cnt, (int)floor(double(freq1[i] / freq2[i])));
            }    
        }
        
        if(cnt == INT_MAX) cnt = 0;
        
        return cnt;
    }
};