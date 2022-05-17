class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> ds;
        
        func(0, s, ds, ans);
        
        return ans;
    }
    
    void func(int i, string s, vector<string> &ds, vector<vector<string>> &ans){
        if(i > s.size()-1){
            ans.push_back(ds);
            return;
        } 
            
        for(int j = i; j < s.size(); j++){
            
            if(isPal(s, i, j) == true){
                ds.push_back(s.substr(i, j -i + 1));
                func(j+1, s, ds, ans);
                ds.pop_back();
            }
        }
        
    }
    
    bool isPal(string s, int start, int end){
        
        while(start<=end){
            if(s[start++] != s[end--]) return false;
        }
        return true;
    }
};