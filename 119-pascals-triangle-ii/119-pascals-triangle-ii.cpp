class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans;
        
        int n = rowIndex;
        long res = 1; 
        ans.push_back(int(res));
        for(int i=0; i<n; i++){
            res *= (n-i);
            res /= (i+1);
            ans.push_back(int(res));
        }
        return ans;
    }
};