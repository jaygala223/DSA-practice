class Solution {
public:
    bool checkPossible(string &s1, string &s2){
        if(s1.size() != s2.size() + 1) return false;
        
        int p1 = 0, p2 = 0;
        
        while(p1 < s1.size()){
            if(s1[p1] == s2[p2]) p2++;
            
            p1++;
        }
        return (p1 == s1.size() and p2 == s2.size());
        
    }
    
    
    static bool comp(string &s1, string &s2){
        return s1.size() < s2.size();
    }
    
    int longestStrChain(vector<string>& arr) {
        int n = arr.size();
        sort(arr.begin(), arr.end(), comp);
        vector<int> dp(n, 1);
        int maxi = 1;
        
        for(int i=0; i<n; i++){
            for(int prev=0; prev<i; prev++){
                
                if(checkPossible(arr[i], arr[prev])){
                    dp[i] = max(1+dp[prev], dp[i]);
                }
            }
            maxi = max(maxi, dp[i]);
        }
        return maxi;
    }
};