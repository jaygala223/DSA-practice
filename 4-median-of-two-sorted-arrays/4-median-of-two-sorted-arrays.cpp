class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        int m=nums1.size();
        int n=nums2.size();
        
        if(m+n == 0) return 0.0;
        vector<int> ans(m+n,0);
        
        int i=m-1,j=n-1,k=m+n-1;
        while(i>=0 and j>=0){
            if(nums2[j]>nums1[i]){
                ans[k--]=nums2[j--];
            }
            else{
                ans[k--]=nums1[i--];
            }
        }
        while(i>=0){
            ans[k--]=nums1[i--];
        }
        while(j>=0){
            ans[k--]=nums2[j--];
        }
        int mid=(m+n)/2;
        if((m+n)%2==0){
            return (ans[mid]+ans[mid-1])/2.0;
        }
        else return ans[mid];
    }
};