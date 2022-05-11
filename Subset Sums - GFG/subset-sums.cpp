// { Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

 // } Driver Code Ends
class Solution
{
public:
    void func(int i, int n, int sum, vector<int> &arr, vector<int> &ans){
        if(i>n-1){
            ans.push_back(sum);
            return;
        }
        sum += arr[i];
        func(i+1, n, sum, arr, ans);
        sum -= arr[i];
        
        func(i+1, n, sum, arr, ans);
    }

    vector<int> subsetSums(vector<int> arr, int N)
    {
        vector<int> ans;
        func(0, N, 0, arr, ans);
        return ans;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        vector<int> arr(N);
        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }
        Solution ob;
        vector<int> ans = ob.subsetSums(arr,N);
        sort(ans.begin(),ans.end());
        for(auto sum : ans){
            cout<< sum<<" ";
        }
        cout<<endl;
    }
    return 0;
}  // } Driver Code Ends