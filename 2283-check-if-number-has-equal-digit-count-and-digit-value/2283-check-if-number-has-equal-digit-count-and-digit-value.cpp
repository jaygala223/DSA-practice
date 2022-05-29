class Solution {
public:
    bool digitCount(string num) {
        unordered_map<char, int> freq;
        
        for(int i=0; i<num.size(); i++){
            freq[num[i]]++;
        }
        
        
        for(int i=0; i<num.size(); i++){
            char ch = '0'+i;
            if(num[i]-'0' != freq[ch]) return false;
        }
        return true;
    }
};