class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        int ans = 0, currTotalTime = 0;
        
        int n = courses.size();
        sort(courses.begin(), courses.end(), [](auto &a, auto &b) {return a[1] < b[1];});
        
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