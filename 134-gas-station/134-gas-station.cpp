class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        
        int n = cost.size();
        vector<int> diff(n,0);
        
        if (accumulate(gas.begin(),gas.end(),0) < accumulate(cost.begin(), cost.end(),0)) return -1;
        
        int total = 0;
        int ansIdx = 0;
        
        for(int i=0; i<n; i++){
            total += gas[i] - cost[i];
            
            if(total < 0){
                total = 0;
                ansIdx = i+1;
            }
        }
        return ansIdx;
    }
};