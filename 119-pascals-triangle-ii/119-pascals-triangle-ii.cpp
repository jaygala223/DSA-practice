class Solution {
public:
    int binomial(int r, int n){
        if(r == 0 or r == n) return 1;
        if(n > n-r) r = n-r;
        
        long ans = 1;
        for(int i=0; i<r; i++){
            ans*= (n-i);
            ans/= (i+1);
        }
        return int(ans);
    }
    
    vector<int> getRow(int rowIndex) {
        vector<int> ans;
        
        for(int i=0; i<=rowIndex; i++){
            ans.push_back(binomial(i, rowIndex));
        }

        return ans;
    }
};