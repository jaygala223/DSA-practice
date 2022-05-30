class Solution {
public:
    int uniquePaths(int m, int n) {
        
        vector<int> prev(n, 0);
        //space optimization
        
        for(int i=0; i<m; i++){
            vector<int> cur(n, 0);
            
            for(int j=0; j<n; j++){
                if(i == 0 and j == 0) {
                    cur[j] = 1;
                    continue;
                }
                
                int up = 0;
                if(i > 0) up = prev[j];
                int left = 0;
                
                if(j > 0) left = cur[j-1];
                cur[j] = left + up;
            }
            prev = cur;
        }
        return prev[n-1];
    }
};