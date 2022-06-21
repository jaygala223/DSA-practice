class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        
        priority_queue<int> hp;
        int i;
        for(i=0; i<n-1; i++){
            int diff = heights[i+1] - heights[i];
            if(diff <= 0) continue;
            else {
                if(bricks >= diff){
                bricks -= diff;
                hp.push(diff);
                }
                else if(ladders > 0){
                    if(hp.size()){
                        int currMax = hp.top();
                        if(currMax > diff){
                            bricks += currMax;
                            hp.pop();
                            hp.push(diff);
                            bricks -= diff;    
                        }
                    }
                    ladders -= 1; 
                }
                else return i;
            }
        }
        return i;
    }
};