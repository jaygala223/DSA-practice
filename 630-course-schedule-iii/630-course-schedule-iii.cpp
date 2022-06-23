class Solution {
public:
    static bool comp(vector<int> a1, vector<int> a2){
        return a1[1] < a2[1];
    }
    
    int scheduleCourse(vector<vector<int>>& courses) {
        int ans = 0, currTotalTime = 0;
        
        int n = courses.size();
        sort(courses.begin(), courses.end(),comp);
        
        priority_queue<int> hp;
        //for(auto course: courses) cout<<course[1]<<" ";
        
        for(auto c: courses){
            
            hp.push(c[0]);
            currTotalTime += c[0];
            
            if(currTotalTime > c[1]){
              currTotalTime -= hp.top();
              hp.pop();  
            } 
            
        }
        return hp.size();
    }
};