// { Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// User function template for C++

class Solution{
    public:
    void func(int i, int j, int n, vector<vector<int>> &visited, string ds, vector<string> &ans, vector<vector<int>> &maze){
        
        if(i == n-1 and j == n-1){
            ans.push_back(ds);
            return;
        }
        
        //down
        if(isValid(i+1, j, visited, n, maze))
        {
            visited[i+1][j] = 1;
            ds.push_back('D');
            func(i+1, j, n, visited, ds, ans, maze);
            ds.pop_back();
            visited[i+1][j] = 0;
        }
        
        //left
        if(isValid(i, j-1, visited, n, maze))
        {
            visited[i][j-1] = 1;
            ds.push_back('L');
            func(i, j-1, n, visited, ds, ans, maze);
            ds.pop_back();
            visited[i][j-1] = 0;
        }
        
        //right
        if(isValid(i, j+1, visited, n, maze))
        {
            visited[i][j+1] = 1;
            ds.push_back('R');
            func(i, j+1, n, visited, ds, ans, maze);
            ds.pop_back();
            visited[i][j+1] = 0;
        }
        
        //up
        if(isValid(i-1, j, visited, n, maze))
        {
            visited[i-1][j] = 1;
            ds.push_back('U');
            func(i-1, j, n, visited, ds, ans, maze);
            ds.pop_back();
            visited[i-1][j] = 0;
        }
        
        
        
    }
    
    bool isValid(int i, int j, vector<vector<int>> &visited, int n, vector<vector<int>> &maze){
        if(i>=0 and j>=0 and i<=n-1 and j<=n-1 and maze[i][j] == 1 and visited[i][j] == 0) return true;
        else return false;
    }
    
    
    vector<string> findPath(vector<vector<int>> &m, int n) {
        
        vector<string> ans;
        string ds;
        
        vector<vector<int>> visited(n, vector<int> (n,0));
        visited[0][0] = 1;
        
        
        if(m[0][0] == 1) func(0,0,n, visited, ds,ans,m);
        
        //if(ans.size() == 0) ans.push_back("-1");
        
        return ans;
    }
};

    


// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int> (n,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m, n);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++) cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}  // } Driver Code Ends