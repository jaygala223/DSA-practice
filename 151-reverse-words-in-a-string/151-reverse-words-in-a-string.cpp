class Solution {
public:
    string reverseWords(string s) {
        string ans = "";
        
        int n = s.size();
        int i = 0, j=0;
        while(i < n){
            while(i<n and s[i] == ' '){
                i++;
            }
            if(i>=n) break;
            j = i+1;
            
            while(j<n and s[j] != ' '){
                j++;
            }
            string sub = s.substr(i, j-i);
            if(ans.size() == 0){
                ans = sub;
            }
            else ans = sub + " " + ans;
            i = j+1;
        }
    
        return ans;
    }
};