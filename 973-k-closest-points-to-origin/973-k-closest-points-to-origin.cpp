class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> ans;
        
        multimap<int,int> mp;
        for(int i=0; i<points.size(); i++){
            mp.insert({pow(points[i][0],2)+ pow(points[i][1],2), i});
        }
        int count = 0;
        for(auto it=mp.begin(); count<k; count++, it++)
            ans.push_back(points[it->second]);
        
        
        return ans;
    }
};