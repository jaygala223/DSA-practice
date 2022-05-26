class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        map<int, int> mp;
        
        for(auto num: tasks){
            mp[num]++;
        }
        
        int freq, ans = 0;
        for(auto i: mp){
            freq = i.second;
            
            if(freq == 1) return -1;
            
            else if(freq % 3 == 0) ans += freq/3;
            
            else{
                ans += freq/3 + 1;
            }
        }
        
        return ans;
    }
};