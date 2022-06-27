class Solution {
public:
    int minPartitions(string n) {
        int maxi = INT_MIN;
        for(auto ch: n){
            maxi = max(maxi, ch - '0');
            if(maxi == 9) return maxi;
        }
        
        return maxi;
    }
};