class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int ans = 0;
        
        for(auto item: sentences){
            int n = item.size();
            int cnt=0;
            for(int i=0; i<n; i++){
                if(item[i] == ' ') cnt++;
            }
            ans = max(cnt,ans);
        }
        return ans+1;
    }
};