class Solution {
public:
    static bool comp(vector<int> &a1, vector<int> &a2){
        return a1[1] > a2[1];
    }
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        int n = boxTypes.size(), ans = 0;
        sort(boxTypes.begin(), boxTypes.end(), comp);
        
        for(int i=0; i<n; i++){
            if(truckSize <= 0) break;
            
            int boxes = boxTypes[i][0];
            int units = boxTypes[i][1];
            
            ans += min(truckSize, boxes) * units;
            truckSize -= boxes;
        }
        return ans;
    }
};