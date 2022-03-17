class Solution {
public:
    bool rotateString(string s, string goal) {
        int n = s.size();
        int m = goal.size();
        
        if(n != m) return false;
        
        for(int i=0; i<n; i++){
            reverse(s.begin(), s.end());
            reverse(s.begin(),s.end()-1);
            
            if(s == goal) return true;
        }
        return false;
    }
};