class Solution {
public:
    string toGoatLatin(string sentence) {
        int aCount = 1;
        
        unordered_set<char> vowel({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'});
        istringstream iss(sentence);
        string ans, word;
        
        while(iss >> word){
            ans += ' ' + (vowel.count(word[0]) == 1 ? word : word.substr(1)+word[0]) + "ma";
            
            for(int i=0; i<aCount; i++) ans += "a";
            aCount++;
        }
        
        //start ka space hatane ke liye
        return ans.substr(1);
    }
};