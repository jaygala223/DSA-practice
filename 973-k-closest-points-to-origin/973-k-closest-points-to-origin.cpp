class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> ans;
        
        priority_queue<vector<int>> heap;
        
        for(auto item: points){
            int x = item[0], y = item[1];
            heap.push({x*x + y*y, x, y});
            
            if(heap.size() > k) heap.pop();
        }
        
        while(!heap.empty()){
            vector<int> top = heap.top();
            heap.pop();
            ans.push_back({top[1],top[2]});
        }
        return ans;
    }
};