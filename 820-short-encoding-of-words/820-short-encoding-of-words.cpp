class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        if(words.size() == 1) return words[0].size()+1;
        
        unordered_set<string> set(words.begin(), words.end());
        
        for(auto word: set){
            for(int ind=1; ind<word.size(); ind++){
                string s = word.substr(ind);
                if(set.find(s) != set.end()) set.erase(s);
            }
        }
        int n = 0;
        for(auto item: set) n+= item.size();
        
        return n+set.size();
    }
};