class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        
        string ans;
        int maxLen = 0, ans_l, ans_r;
        
        for(int i=0; i<n; i++){
            
            //odd
            int left = i, right = i;
            while(left >=0 and right < n and s[left] == s[right]){
                int currLen = right - left + 1;
                if(currLen > maxLen){
                    maxLen = currLen;
                    ans_l = left, ans_r = right;
                }
                left--;
                right++;
            }
            
            //even
            left = i, right = i+1;
            while(left >=0 and right < n and s[left] == s[right]){
                int currLen = right - left + 1;
                if(currLen > maxLen){
                    maxLen = currLen;
                    ans_l = left, ans_r = right;
                }
                left--;
                right++;
            }
        }
        return s.substr(ans_l, maxLen);
    }
};