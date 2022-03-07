class Solution {
public:
    
    
    int climbStairs(int n) {
        if(n<=2) return n;
        
        int prev2 = 1;
        int prev = 2;
        int curr_i=0;
        
        for(int i=2; i<n; i++){
            curr_i = prev2 + prev;
            prev2 = prev;
            prev = curr_i;
        }
        
        return prev;
    }
};