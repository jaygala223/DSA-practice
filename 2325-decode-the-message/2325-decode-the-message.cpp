class Solution {
public:
    string decodeMessage(string key, string message) {
        
        map<char, char> mp;
        
        char letter = 'a'-1;
        
        for(auto it: key){
            if(it == ' ') continue;
            if(mp.find(it) != mp.end()) continue;
            mp[it] = letter++;
        }
        
        string s;
        for(int i=0; i<message.size(); i++){
            if(message[i] == ' ') s.push_back(' ');
            else{
                s.push_back(mp[message[i]]+1);
            }
        }
        return s;
    }
};