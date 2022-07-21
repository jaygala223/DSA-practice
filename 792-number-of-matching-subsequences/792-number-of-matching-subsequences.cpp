class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        map<char, vector<int>> mp;
        int ans = 0;
        int i=0;
        for(auto ch: s) mp[ch].push_back(i++);
        
        for(auto word: words){
            int last_occurence = -1;
            int k = 0;
            
            for(k=0; k<word.size(); k++){
                auto it = upper_bound(mp[word[k]].begin(), mp[word[k]].end(), last_occurence);
                
                //koi suitable value nahi mili break karde re baba
                if(it == mp[word[k]].end()) break;
                
                //kyuki 'it' ek pointer hai
                last_occurence = *it;
                if(k == word.size()-1) ans++;
            }
        }
        return ans;
    }
};