class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        if(words.size() == 1) return words[0].size()+1;
        
        unordered_set<string> set;
        for(auto item: words){set.insert(item);}
        
        for(int i=0; i<words.size(); i++){
            for(int ind=1; ind<words[i].size(); ind++){
                string s = words[i].substr(ind, words[i].size()-1);
                if(set.find(s) != set.end()) set.erase(s);
            }
        }
        int n = 0, cnt = 0;
        for(auto item: set) n+= item.size();
        
        return n+set.size();
    }
};