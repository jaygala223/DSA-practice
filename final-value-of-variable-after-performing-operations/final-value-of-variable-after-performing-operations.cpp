class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int ans = 0;
        
        for(auto item: operations){
            if(item == "++X" || item == "X++") ans++;
            else ans--;
        }
        return ans;
    }
};